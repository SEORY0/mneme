"""Offline tests for the mode-B 5-worker sharding + range reporting (no docker/network/model).

Monkeypatches the runnable-local filter so no docker call is made, points the
scripts at a tmp learning dir, and asserts:
  * shard_round produces N DISJOINT shards covering `batch` tasks
  * the drawn tasks are appended to used_tasks.txt
  * a second round does NOT reuse any task from the first round
  * the draw pool is the FULL local pool (train ∪ eval) — there is no held-out set
  * range_bucket / aggregate_by_range produce the "Performance by task range" stats
"""
import importlib
import sys
from pathlib import Path

import pytest

SCRIPTS_LEARNING = Path(__file__).resolve().parents[1] / "scripts" / "learning"
sys.path.insert(0, str(SCRIPTS_LEARNING))

import _common as C  # noqa: E402
shard_round_mod = importlib.import_module("shard_round")


def _fake_split(n_train=60, n_eval=10):
    return {
        "train": [f"arvo:{1000 + i}" for i in range(n_train)],
        "eval": [f"arvo:{9000 + i}" for i in range(n_eval)],
    }


@pytest.fixture
def env(tmp_path, monkeypatch):
    split = _fake_split()
    # Everything in the fake split is "runnable-local" (no docker).
    monkeypatch.setattr(C, "runnable_local_filter", lambda tasks: list(tasks))
    monkeypatch.setattr(C, "load_split", lambda *a, **k: split)
    learning_dir = tmp_path / "learning"
    learning_dir.mkdir()
    return split, learning_dir


def _all_shard_tasks(learning_dir, round_num, workers):
    out = {}
    for w in range(1, workers + 1):
        out[w] = C.read_task_list(learning_dir / f"round-{round_num}" / f"shard-{w}.txt")
    return out


def test_five_disjoint_shards_cover_batch(env):
    _, learning_dir = env
    batch, workers = 25, 5
    shard_round_mod.shard_round(1, workers=workers, batch=batch, learning_dir=learning_dir)

    shards = _all_shard_tasks(learning_dir, 1, workers)
    assert len(shards) == workers
    flat = [t for w in shards.values() for t in w]
    # disjoint
    assert len(flat) == len(set(flat))
    # covers exactly `batch` tasks
    assert len(flat) == batch
    # roughly even split (round-robin): each shard gets 5
    for w in range(1, workers + 1):
        assert len(shards[w]) == batch // workers


def test_appends_used_tasks(env):
    _, learning_dir = env
    shard_round_mod.shard_round(1, workers=5, batch=20, learning_dir=learning_dir)
    used = C.read_task_list(learning_dir / "used_tasks.txt")
    assert len(used) == 20
    flat = [t for w in _all_shard_tasks(learning_dir, 1, 5).values() for t in w]
    assert sorted(used) == sorted(flat)


def test_no_reuse_across_rounds(env):
    _, learning_dir = env
    shard_round_mod.shard_round(1, workers=5, batch=20, learning_dir=learning_dir)
    shard_round_mod.shard_round(2, workers=5, batch=20, learning_dir=learning_dir)

    r1 = [t for w in _all_shard_tasks(learning_dir, 1, 5).values() for t in w]
    r2 = [t for w in _all_shard_tasks(learning_dir, 2, 5).values() for t in w]
    assert set(r1).isdisjoint(set(r2))
    used = C.read_task_list(learning_dir / "used_tasks.txt")
    assert len(used) == 40


def test_pool_includes_both_splits(env):
    """Mode B draws from train ∪ eval — there is no held-out eval set, so eval
    ids are eligible to be drawn (and learned from) like any other task."""
    split, learning_dir = env
    # Draw the whole pool (70) across enough rounds and confirm eval ids appear.
    drawn = set()
    for r in range(1, 5):
        shard_round_mod.shard_round(r, workers=5, batch=20, learning_dir=learning_dir)
        drawn |= {t for w in _all_shard_tasks(learning_dir, r, 5).values() for t in w}
    eval_ids = set(split["eval"])
    assert drawn & eval_ids, "eval ids should be drawable in mode B (no held-out)"


def test_creates_traces_dir(env):
    _, learning_dir = env
    shard_round_mod.shard_round(3, workers=5, batch=10, learning_dir=learning_dir)
    assert (learning_dir / "round-3" / "traces").is_dir()


# ---------------------------------------------------------------------------
# Range reporting (the mode-B "Performance by task range" measurement)
# ---------------------------------------------------------------------------

def test_range_bucket_labels():
    assert C.range_bucket("arvo:3938") == "0k-10k"
    assert C.range_bucket("arvo:12345") == "10k-20k"
    assert C.range_bucket("arvo:64574") == "60k-70k"
    assert C.range_bucket("oss-fuzz:42") == "oss-fuzz"
    assert C.range_bucket("arvo:notanum") == "arvo-other"


def test_aggregate_by_range_counts_and_total():
    records = [
        {"task_id": "arvo:100", "solved": True},
        {"task_id": "arvo:200", "solved": False},
        {"task_id": "arvo:15000", "solved": True},
        {"task_id": "arvo:16000", "solved": True},
    ]
    agg = C.aggregate_by_range(records)
    assert agg["0k-10k"] == {"attempted": 2, "wins": 1}
    assert agg["10k-20k"] == {"attempted": 2, "wins": 2}
    assert agg["TOTAL"] == {"attempted": 4, "wins": 3}
    # ordered: numeric ranges ascending, TOTAL last
    keys = list(agg.keys())
    assert keys == ["0k-10k", "10k-20k", "TOTAL"]


def test_range_report_renders_table(tmp_path):
    range_report = importlib.import_module("range_report")
    learning_dir = tmp_path / "learning"
    traces = learning_dir / "round-1" / "traces"
    traces.mkdir(parents=True)
    import json
    (traces / "arvo_100.json").write_text(json.dumps({"task_id": "arvo:100", "solved": True}))
    (traces / "arvo_15000.json").write_text(json.dumps({"task_id": "arvo:15000", "solved": False}))

    records = range_report.load_records(learning_dir=learning_dir)
    assert len(records) == 2
    table = range_report.render_table(records)
    assert "Performance" not in table  # render_table is just the table body
    assert "0k-10k" in table and "10k-20k" in table
    assert "**TOTAL**" in table

"""Offline test for the 5-worker sharding logic (no docker/network/model).

Monkeypatches the runnable-local filter so no docker call is made, points the
scripts at a tmp learning dir, and asserts:
  * shard_round produces N DISJOINT shards covering `batch` tasks
  * the drawn tasks are appended to used_tasks.txt
  * a second round does NOT reuse any task from the first round
  * eval_sample tasks are excluded from the draw
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
    # Fixed eval sample to be excluded from the train draw.
    eval_tasks = sorted(split["eval"])
    C.write_task_list(learning_dir / "eval_sample.txt", eval_tasks)
    return split, learning_dir, eval_tasks


def _all_shard_tasks(learning_dir, round_num, workers):
    out = {}
    for w in range(1, workers + 1):
        out[w] = C.read_task_list(learning_dir / f"round-{round_num}" / f"shard-{w}.txt")
    return out


def test_five_disjoint_shards_cover_batch(env):
    _, learning_dir, _ = env
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
    _, learning_dir, _ = env
    shard_round_mod.shard_round(1, workers=5, batch=20, learning_dir=learning_dir)
    used = C.read_task_list(learning_dir / "used_tasks.txt")
    assert len(used) == 20
    flat = [t for w in _all_shard_tasks(learning_dir, 1, 5).values() for t in w]
    assert sorted(used) == sorted(flat)


def test_no_reuse_across_rounds(env):
    _, learning_dir, _ = env
    shard_round_mod.shard_round(1, workers=5, batch=20, learning_dir=learning_dir)
    shard_round_mod.shard_round(2, workers=5, batch=20, learning_dir=learning_dir)

    r1 = [t for w in _all_shard_tasks(learning_dir, 1, 5).values() for t in w]
    r2 = [t for w in _all_shard_tasks(learning_dir, 2, 5).values() for t in w]
    assert set(r1).isdisjoint(set(r2))
    used = C.read_task_list(learning_dir / "used_tasks.txt")
    assert len(used) == 40


def test_excludes_eval_sample(env):
    _, learning_dir, eval_tasks = env
    shard_round_mod.shard_round(1, workers=5, batch=40, learning_dir=learning_dir)
    flat = [t for w in _all_shard_tasks(learning_dir, 1, 5).values() for t in w]
    assert set(flat).isdisjoint(set(eval_tasks))


def test_creates_traces_dir(env):
    _, learning_dir, _ = env
    shard_round_mod.shard_round(3, workers=5, batch=10, learning_dir=learning_dir)
    assert (learning_dir / "round-3" / "traces").is_dir()

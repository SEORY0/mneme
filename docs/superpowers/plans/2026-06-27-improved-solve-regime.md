# Improved Solve Regime Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Raise mneme's prequential solve rate by attacking under-iteration — give each task a fresh small-shard context, harness-enforce a ≥N distinct-candidate floor before a `no_crash` loss, and re-dispatch unsolved tasks best-of-k.

**Architecture:** Three isolated mechanism changes in the no-API learning loop: (1) `shard_round.py` chunks a round's batch into contiguous `SHARD_SIZE` shards (decoupled from concurrency); (2) `runner verify` logs every distinct candidate to `learning/round-$R/attempts.jsonl`, and `_common.py` exposes an `attempt_gate`; (3) `run_pass.sh` derives the shard count dynamically, runs a concurrency-capped launcher, and re-dispatches any task that is neither solved nor floor-met, up to `k` times.

**Tech Stack:** Python 3 (typer CLI, pytest), Bash. No new dependencies.

## Global Constraints

- No LLM API inside mneme — workers write PoC bytes themselves; harness provides only `gen`/`verify`/`submit` + OKF memory.
- Workers never touch git; only the consolidator commits, on the current branch (never switches branches).
- CyberGym Level-1 rules unchanged (tier-1 vul-image verify; official `submit` scoring; promotion redaction).
- Defaults, env-overridable: `SHARD_SIZE=3`, `CONCURRENCY=5`, `N=5` (distinct candidates before a `no_crash` loss is acceptable), `k=2` (max independent dispatches per task).
- Backward compatibility: `runner verify` must keep working when `ROUND` is unset (non-learning callers) — it then skips attempt logging.
- All tests offline: no docker, no network, no model. Monkeypatch docker-touching helpers.
- `.venv/bin/python` is the interpreter; `.venv/bin/python -m pytest -q` must stay green.

---

### Task 1: Attempt-logging + gate helpers in `_common.py`

**Files:**
- Modify: `scripts/learning/_common.py` (append new helpers after `aggregate_by_range`)
- Test: `tests/test_attempt_gate.py` (new)

**Interfaces:**
- Consumes: `LEARNING_DIR` (existing module global), `read_task_list` (existing).
- Produces:
  - `SHARD_SIZE: int` (default 3, from env `MNEME_SHARD_SIZE`)
  - `CONCURRENCY: int` (default 5, from env `MNEME_CONCURRENCY`)
  - `ATTEMPT_FLOOR_N: int` (default 5, from env `MNEME_ATTEMPT_FLOOR`)
  - `BEST_OF_K: int` (default 2, from env `MNEME_BEST_OF_K`)
  - `attempts_path(round_num: int, learning_dir: Path|None=None) -> Path`
  - `record_attempt(round_num: int, task_id: str, candidate_sha256: str, failure_class: str, learning_dir: Path|None=None) -> None`
  - `distinct_candidates(round_num: int, task_id: str, learning_dir: Path|None=None) -> int`
  - `attempt_gate(round_num: int, task_id: str, solved: bool, n: int|None=None, learning_dir: Path|None=None) -> bool`

- [ ] **Step 1: Write the failing test**

Create `tests/test_attempt_gate.py`:

```python
"""Offline tests for the harness-enforced attempt floor (no docker/network)."""
import sys
from pathlib import Path

SCRIPTS_LEARNING = Path(__file__).resolve().parents[1] / "scripts" / "learning"
sys.path.insert(0, str(SCRIPTS_LEARNING))

import _common as C  # noqa: E402


def test_record_and_count_distinct_candidates(tmp_path):
    ld = tmp_path / "learning"
    C.record_attempt(1, "arvo:100", "aaa", "no_crash", learning_dir=ld)
    C.record_attempt(1, "arvo:100", "bbb", "no_crash", learning_dir=ld)
    C.record_attempt(1, "arvo:100", "aaa", "no_crash", learning_dir=ld)  # duplicate sha
    C.record_attempt(1, "arvo:200", "ccc", "wrong_sink", learning_dir=ld)
    assert C.distinct_candidates(1, "arvo:100", learning_dir=ld) == 2  # aaa,bbb (dup ignored)
    assert C.distinct_candidates(1, "arvo:200", learning_dir=ld) == 1
    assert C.distinct_candidates(1, "arvo:999", learning_dir=ld) == 0


def test_attempt_gate_accepts_solved_regardless_of_count(tmp_path):
    ld = tmp_path / "learning"
    # zero attempts logged, but solved -> accepted
    assert C.attempt_gate(1, "arvo:100", solved=True, n=5, learning_dir=ld) is True


def test_attempt_gate_requires_n_distinct_when_unsolved(tmp_path):
    ld = tmp_path / "learning"
    for sha in ["a", "b", "c", "d"]:  # only 4 distinct
        C.record_attempt(1, "arvo:100", sha, "no_crash", learning_dir=ld)
    assert C.attempt_gate(1, "arvo:100", solved=False, n=5, learning_dir=ld) is False
    C.record_attempt(1, "arvo:100", "e", "no_crash", learning_dir=ld)  # now 5
    assert C.attempt_gate(1, "arvo:100", solved=False, n=5, learning_dir=ld) is True


def test_attempt_gate_default_n_is_module_floor(tmp_path):
    ld = tmp_path / "learning"
    assert C.ATTEMPT_FLOOR_N == 5
    assert C.attempt_gate(1, "arvo:100", solved=False, learning_dir=ld) is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_attempt_gate.py -q`
Expected: FAIL with `AttributeError: module '_common' has no attribute 'record_attempt'`

- [ ] **Step 3: Write minimal implementation**

Append to `scripts/learning/_common.py` (after `aggregate_by_range`). Note `json` and `os` are already imported at the top of the file:

```python
# ---------------------------------------------------------------------------
# Solve-regime knobs + harness-enforced attempt floor (best-of-k support)
# ---------------------------------------------------------------------------
SHARD_SIZE = int(os.environ.get("MNEME_SHARD_SIZE", "3"))
CONCURRENCY = int(os.environ.get("MNEME_CONCURRENCY", "5"))
ATTEMPT_FLOOR_N = int(os.environ.get("MNEME_ATTEMPT_FLOOR", "5"))
BEST_OF_K = int(os.environ.get("MNEME_BEST_OF_K", "2"))


def attempts_path(round_num: int, learning_dir: Path | None = None) -> Path:
    learning_dir = learning_dir or LEARNING_DIR
    return learning_dir / f"round-{round_num}" / "attempts.jsonl"


def record_attempt(round_num: int, task_id: str, candidate_sha256: str,
                   failure_class: str, learning_dir: Path | None = None) -> None:
    """Append one verified-candidate record. Tamper-evident: the worker must
    actually run `verify` on a distinct file to add a distinct sha."""
    p = attempts_path(round_num, learning_dir)
    p.parent.mkdir(parents=True, exist_ok=True)
    rec = {"task_id": task_id, "candidate_sha256": candidate_sha256,
           "failure_class": failure_class}
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")


def distinct_candidates(round_num: int, task_id: str,
                        learning_dir: Path | None = None) -> int:
    """Count distinct candidate_sha256 logged for a task this round."""
    p = attempts_path(round_num, learning_dir)
    if not p.exists():
        return 0
    shas = set()
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("task_id") == task_id and rec.get("candidate_sha256"):
            shas.add(rec["candidate_sha256"])
    return len(shas)


def attempt_gate(round_num: int, task_id: str, solved: bool,
                 n: int | None = None, learning_dir: Path | None = None) -> bool:
    """A task outcome is acceptable iff solved, or >= n distinct candidates tried."""
    if solved:
        return True
    n = ATTEMPT_FLOOR_N if n is None else n
    return distinct_candidates(round_num, task_id, learning_dir) >= n
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_attempt_gate.py -q`
Expected: PASS (4 passed)

- [ ] **Step 5: Commit**

```bash
git add scripts/learning/_common.py tests/test_attempt_gate.py
git commit -m "feat(learning): attempt-floor helpers (record/distinct/gate) + knobs"
```

---

### Task 2: `runner verify` logs each distinct candidate

**Files:**
- Modify: `runner/run.py` (the `verify` command body — after `rv = verify_core.run(...)`, before/after building `out`)
- Test: `tests/test_verify_attempt_log.py` (new)

**Interfaces:**
- Consumes: `_common.record_attempt` (Task 1); `run_dir/gen_info.json` `task_id` field (written by `gen`); env `ROUND`.
- Produces: side effect only — appends to `learning/round-$ROUND/attempts.jsonl` when `ROUND` is set.

**Context:** `verify` currently takes `--run-dir`/`--poc`, reads `verify_config.json`, runs `verify_core.run`, and prints a JSON `out` dict with `failure_class`. We add logging WITHOUT changing its stdout or signature. `task_id` is read from `run_dir/gen_info.json` (written by `gen`). Round comes from the `ROUND` env (the worker exports it); if unset or gen_info missing, skip logging silently so non-learning callers are unaffected.

- [ ] **Step 1: Write the failing test**

Create `tests/test_verify_attempt_log.py`:

```python
"""verify logs a distinct-candidate attempt when ROUND is set (no docker)."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "learning"))
import _common as C  # noqa: E402

import runner.run as run  # noqa: E402


def _fake_verdict():
    return SimpleNamespace(
        failure_class="no_crash", target_likelihood=0.0, crash_type=None,
        sink_fn=None, sink_loc=None, parser_reached=True, output_excerpt="clean",
    )


def test_verify_logs_attempt_when_round_set(tmp_path, monkeypatch):
    run_dir = tmp_path / "runs" / "s1_arvo_100"
    run_dir.mkdir(parents=True)
    (run_dir / "verify_config.json").write_text(json.dumps({
        "vul_image": "img", "run_cmd": "/bin/arvo", "timeout_s": 30, "description": "d"}))
    (run_dir / "gen_info.json").write_text(json.dumps({"task_id": "arvo:100"}))
    poc = run_dir / "poc"
    poc.write_bytes(b"AAAA")

    # no docker: stub verify_core.run
    monkeypatch.setattr(run, "_load_env", lambda: None, raising=False)
    import mneme.verify_core as vc
    monkeypatch.setattr(vc, "run", lambda *a, **k: _fake_verdict())

    ld = tmp_path / "learning"
    monkeypatch.setenv("ROUND", "7")
    monkeypatch.setattr(C, "LEARNING_DIR", ld)

    run.verify(run_dir=run_dir, poc=poc, confirm=False)

    assert C.distinct_candidates(7, "arvo:100", learning_dir=ld) == 1
    # same bytes again -> still 1 distinct; different bytes -> 2
    run.verify(run_dir=run_dir, poc=poc, confirm=False)
    assert C.distinct_candidates(7, "arvo:100", learning_dir=ld) == 1
    poc.write_bytes(b"BBBB")
    run.verify(run_dir=run_dir, poc=poc, confirm=False)
    assert C.distinct_candidates(7, "arvo:100", learning_dir=ld) == 2


def test_verify_no_log_when_round_unset(tmp_path, monkeypatch):
    run_dir = tmp_path / "runs" / "s1_arvo_100"
    run_dir.mkdir(parents=True)
    (run_dir / "verify_config.json").write_text(json.dumps({
        "vul_image": "img", "run_cmd": "/bin/arvo", "timeout_s": 30, "description": "d"}))
    (run_dir / "gen_info.json").write_text(json.dumps({"task_id": "arvo:100"}))
    poc = run_dir / "poc"; poc.write_bytes(b"AAAA")
    import mneme.verify_core as vc
    monkeypatch.setattr(vc, "run", lambda *a, **k: _fake_verdict())
    monkeypatch.delenv("ROUND", raising=False)
    ld = tmp_path / "learning"
    monkeypatch.setattr(C, "LEARNING_DIR", ld)
    run.verify(run_dir=run_dir, poc=poc, confirm=False)
    assert C.distinct_candidates(7, "arvo:100", learning_dir=ld) == 0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_verify_attempt_log.py -q`
Expected: FAIL (verify does not log; `distinct_candidates == 0` where 1 is expected)

- [ ] **Step 3: Write minimal implementation**

In `runner/run.py`, inside the `verify` command, after the `out` dict is built (and before the `confirm` block / final `typer.echo`), add the logging. First ensure the module can import `_common`; at the TOP of `verify`'s body add a helper-local import and a sha. Insert this block right after `out = { ... }` is constructed:

```python
    # Harness attempt log (best-of-k floor). Only when a round context is set.
    _round = os.environ.get("ROUND")
    if _round and _round.isdigit():
        try:
            import hashlib
            sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "learning"))
            import _common as _C
            gi = json.loads((run_dir / "gen_info.json").read_text(encoding="utf-8"))
            _tid = gi.get("task_id")
            if _tid:
                _sha = hashlib.sha256(Path(poc).read_bytes()).hexdigest()
                _C.record_attempt(int(_round), _tid, _sha, rv.failure_class)
        except (OSError, json.JSONDecodeError):
            pass  # logging is best-effort; never break verify
```

Ensure `import os`, `import sys`, `import json`, and `from pathlib import Path` exist at the top of `runner/run.py` (add any that are missing).

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_verify_attempt_log.py -q`
Expected: PASS (2 passed)

- [ ] **Step 5: Run the full suite to confirm no regression**

Run: `.venv/bin/python -m pytest -q`
Expected: PASS (all green)

- [ ] **Step 6: Commit**

```bash
git add runner/run.py tests/test_verify_attempt_log.py
git commit -m "feat(learning): verify logs distinct candidates to attempts.jsonl"
```

---

### Task 3: `shard_round.py` chunks by `SHARD_SIZE` (decoupled from worker count)

**Files:**
- Modify: `scripts/learning/shard_round.py` (the `shard_round` function + CLI args)
- Test: `tests/test_learning_shard.py` (add cases; existing tests use `workers=5` and must still pass via a back-compat path)

**Interfaces:**
- Consumes: `_common.local_pool`, `_common.SHARD_SIZE`, `_common.write_task_list`, `_common.append_task_list`.
- Produces: `shard_round(round_num, *, shard_size=None, workers=None, batch=50, seed_base=770000, learning_dir=None) -> dict` writing `shard-1..M.txt` where `M = ceil(len(drawn)/shard_size)`; returns `{"shards": {i: [ids]}, "drawn": [...], "num_shards": M}`.

**Decision:** Keep a `workers` kwarg for back-compat (existing tests pass `workers=5`), but when `shard_size` is given it takes precedence and shards are CONTIGUOUS chunks of `shard_size`. Default behavior (no args) uses `C.SHARD_SIZE`.

- [ ] **Step 1: Write the failing test**

Add to `tests/test_learning_shard.py`:

```python
def test_shard_size_contiguous_chunks(env, monkeypatch):
    _, learning_dir = env
    import importlib
    monkeypatch.setattr(C, "SHARD_SIZE", 3)
    shard_round_mod.shard_round(1, batch=20, learning_dir=learning_dir)
    # ceil(20/3) = 7 shards: six of 3, one of 2
    shard_files = sorted((learning_dir / "round-1").glob("shard-*.txt"))
    assert len(shard_files) == 7
    sizes = [len(C.read_task_list(f)) for f in shard_files]
    assert sorted(sizes, reverse=True) == [3, 3, 3, 3, 3, 3, 2]
    flat = [t for f in shard_files for t in C.read_task_list(f)]
    assert len(flat) == len(set(flat)) == 20
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_learning_shard.py::test_shard_size_contiguous_chunks -q`
Expected: FAIL (currently splits round-robin into a fixed 5 shards, so 5 files not 7)

- [ ] **Step 3: Write minimal implementation**

Replace the body of `shard_round` in `scripts/learning/shard_round.py`. The draw logic (pool, used, seeded shuffle, `drawn`) is unchanged; only the splitting changes:

```python
def shard_round(round_num: int, workers: int = None, batch: int = 50,
                seed_base: int = 770000, learning_dir: Path = None,
                shard_size: int = None) -> dict:
    import math
    learning_dir = learning_dir or C.LEARNING_DIR
    used_path = learning_dir / "used_tasks.txt"
    shard_size = shard_size if shard_size is not None else C.SHARD_SIZE

    pool = C.local_pool()
    used = set(C.read_task_list(used_path))
    available = sorted(set(pool) - used)
    if not available:
        raise SystemExit("no available tasks left (local pool exhausted)")

    rng = random.Random(seed_base + round_num)
    rng.shuffle(available)
    drawn = sorted(available[:batch])

    round_dir = learning_dir / f"round-{round_num}"
    (round_dir / "traces").mkdir(parents=True, exist_ok=True)

    # CONTIGUOUS chunks of shard_size (fresh context per ~shard_size tasks).
    num_shards = max(1, math.ceil(len(drawn) / shard_size))
    shards: dict[int, list[str]] = {}
    for i in range(num_shards):
        shards[i + 1] = drawn[i * shard_size:(i + 1) * shard_size]

    for w, tasks in shards.items():
        C.write_task_list(round_dir / f"shard-{w}.txt", tasks)

    C.append_task_list(used_path, drawn)

    print(f"Round {round_num}: drew {len(drawn)} tasks into {num_shards} shards "
          f"(size {shard_size}); now {len(C.read_task_list(used_path))} used.")
    return {"shards": shards, "drawn": drawn, "num_shards": num_shards}
```

Update the CLI parser at the bottom of the file: add `--shard-size` (type int, default None) and pass it through; keep `--workers` accepted-but-ignored-when-shard-size-set for back-compat. Locate the existing `argparse` block and add:

```python
    ap.add_argument("--shard-size", type=int, default=None,
                    help="tasks per shard (default _common.SHARD_SIZE=3)")
```
and change the call to `shard_round(args.round, workers=args.workers, batch=args.batch, seed_base=args.seed_base, learning_dir=None, shard_size=args.shard_size)`.

- [ ] **Step 4: Fix the back-compat tests**

The existing tests (`test_five_disjoint_shards_cover_batch`, etc.) call `shard_round(..., workers=5, batch=25)` and assert 5 shards of 5. Under the new default `SHARD_SIZE=3` they'd get `ceil(25/3)=9` shards. Update those tests to pass `shard_size=` explicitly so they assert the intended geometry. For `test_five_disjoint_shards_cover_batch` change the call to `shard_round_mod.shard_round(1, batch=25, learning_dir=learning_dir, shard_size=5)` and keep the `== 5` shard / `== 5` per-shard assertions. For `test_appends_used_tasks`, `test_no_reuse_across_rounds`, `test_pool_includes_both_splits`, `test_creates_traces_dir`: add `shard_size=4` (or any value) to the calls — they only assert used_tasks counts / disjointness / dir creation, which are size-independent.

- [ ] **Step 5: Run tests to verify all pass**

Run: `.venv/bin/python -m pytest tests/test_learning_shard.py -q`
Expected: PASS (all, including the new contiguous-chunk test)

- [ ] **Step 6: Commit**

```bash
git add scripts/learning/shard_round.py tests/test_learning_shard.py
git commit -m "feat(learning): shard_round chunks by SHARD_SIZE (decouple from worker count)"
```

---

### Task 4: `run_pass.sh` — dynamic shard count, concurrency cap, best-of-k re-dispatch

**Files:**
- Modify: `scripts/learning/run_pass.sh` (`do_round`, `worker_wave`, `run_worker`, `shard_complete`, `round_complete`)
- Test: `tests/test_run_pass_gate.sh` (new — a small bash harness; bash logic is verified by running the gate functions against fixture dirs, no codex/docker)

**Interfaces:**
- Consumes: `_common.attempt_gate`, `_common.distinct_candidates`, `_common.CONCURRENCY`, `_common.BEST_OF_K` (read into bash via a one-line python eval at startup).
- Produces: a run loop where each shard's tasks are accepted only when solved-or-floor-met, with ≤k dispatches per task.

**Context:** Bash is hard to unit-test in the pytest sense; this task uses a focused bash test script that exercises the *acceptance gate* (the risky logic) with fixture `attempts.jsonl`/trace files, plus a `bash -n` syntax gate. The concurrency launcher and re-dispatch are verified by `bash -n` + a dry-run with a stubbed `run_worker`.

**Design notes for the implementer:**
- Read knobs once near the top: `CONCURRENCY=$(.venv/bin/python -c 'import sys;sys.path.insert(0,"scripts/learning");import _common as C;print(C.CONCURRENCY)')` and likewise `BEST_OF_K`.
- Replace fixed `WORKERS` iteration with a glob over `learning/round-$R/shard-*.txt` to get the shard list.
- A shard is "accepted" when EVERY task in it is `attempt_gate`-true. `shard_complete` must call the gate, not just check trace existence:
  add a bash helper `task_accepted R task` that runs
  `.venv/bin/python -c 'import sys;sys.path.insert(0,"scripts/learning");import _common as C,json,glob;...'`
  returning 0/1 from `attempt_gate(R, task, solved)`, where `solved` is read from the task's trace JSON (`learning/round-$R/traces/<safe>.json`).
- Re-dispatch: maintain a per-task dispatch counter file `learning/round-$R/dispatch/<safe>.cnt`. Before launching a shard, drop tasks already accepted; for unaccepted tasks whose count `< BEST_OF_K`, include them and increment; tasks at `== BEST_OF_K` are recorded as `under_floor` losses and excluded.
- Concurrency: launch shard sessions in a pool capped at `CONCURRENCY` (loop launching while `jobs -r | wc -l` < CONCURRENCY; `wait -n` to drain).

- [ ] **Step 1: Write the failing test (gate logic)**

Create `tests/test_run_pass_gate.sh`:

```bash
#!/usr/bin/env bash
# Exercises the run_pass acceptance gate against fixtures (no codex/docker).
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
LD="$(mktemp -d)/learning"; mkdir -p "$LD/round-9/traces"
# task A: solved -> accepted regardless of attempts
echo '{"task_id":"arvo:1","solved":true}' > "$LD/round-9/traces/arvo_1.json"
# task B: unsolved, 5 distinct attempts -> accepted
for s in a b c d e; do echo "{\"task_id\":\"arvo:2\",\"candidate_sha256\":\"$s\",\"failure_class\":\"no_crash\"}" >> "$LD/round-9/attempts.jsonl"; done
echo '{"task_id":"arvo:2","solved":false}' > "$LD/round-9/traces/arvo_2.json"
# task C: unsolved, 3 distinct attempts -> NOT accepted
for s in a b c; do echo "{\"task_id\":\"arvo:3\",\"candidate_sha256\":\"$s\",\"failure_class\":\"no_crash\"}" >> "$LD/round-9/attempts.jsonl"; done
echo '{"task_id":"arvo:3","solved":false}' > "$LD/round-9/traces/arvo_3.json"

gate(){ MNEME_LEARNING_OVERRIDE="$LD" .venv/bin/python -c '
import sys,glob,json;sys.path.insert(0,"scripts/learning");import _common as C
from pathlib import Path
ld=Path("'"$LD"'");R=9;tid=sys.argv[1]
safe=tid.replace(":","_")
tr=json.load(open(ld/f"round-{R}/traces/{safe}.json"))
print("YES" if C.attempt_gate(R,tid,tr.get("solved"),learning_dir=ld) else "NO")' "$1"; }

[ "$(gate arvo:1)" = YES ] || { echo "FAIL: arvo:1 should be accepted (solved)"; fail=1; }
[ "$(gate arvo:2)" = YES ] || { echo "FAIL: arvo:2 should be accepted (5 distinct)"; fail=1; }
[ "$(gate arvo:3)" = NO  ] || { echo "FAIL: arvo:3 should be rejected (3 distinct)"; fail=1; }
[ "$fail" = 0 ] && echo "PASS: gate logic" || exit 1
```

- [ ] **Step 2: Run it to verify it fails**

Run: `bash tests/test_run_pass_gate.sh`
Expected: FAIL — `attempt_gate` ignores the passed `learning_dir` for trace lookups? No: it fails first because `run_pass.sh` gate wiring doesn't exist yet AND we must confirm `attempt_gate(... learning_dir=ld)` reads `round-9/attempts.jsonl` under `ld`. If the helpers from Task 1 are in place, this test actually PASSES already (it tests `_common.attempt_gate` directly). Treat Step 2 as: run it, and if it passes, that confirms the gate helper is correct — proceed to wire it into bash. If it fails, fix `attempt_gate`/`distinct_candidates` to honor `learning_dir`.

- [ ] **Step 3: Implement the bash wiring**

Edit `scripts/learning/run_pass.sh`:

1. After the knob/`EXPECT_BRANCH` setup, add:
```bash
CONCURRENCY="$(.venv/bin/python -c 'import sys;sys.path.insert(0,"scripts/learning");import _common as C;print(C.CONCURRENCY)' 2>/dev/null || echo 5)"
BEST_OF_K="$(.venv/bin/python -c 'import sys;sys.path.insert(0,"scripts/learning");import _common as C;print(C.BEST_OF_K)' 2>/dev/null || echo 2)"
```
2. Add a gate helper:
```bash
task_accepted(){  # R safe_task task_id  -> 0 if accepted (solved or floor met)
  local r="$1" safe="$2" tid="$3" tr="learning/round-$r/traces/$2.json"
  [ -f "$tr" ] || return 1
  .venv/bin/python - "$r" "$tid" "$tr" <<'PY'
import sys,json;sys.path.insert(0,"scripts/learning");import _common as C
r=int(sys.argv[1]);tid=sys.argv[2];tr=json.load(open(sys.argv[3]))
sys.exit(0 if C.attempt_gate(r,tid,tr.get("solved")) else 1)
PY
}
```
3. Rewrite `shard_complete` to require ACCEPTANCE (not mere trace existence) for every task in the shard, using `task_accepted` with `safe_task`.
4. Rewrite `round_complete` to glob `learning/round-$R/shard-*.txt` (dynamic count) instead of `seq 1 $WORKERS`.
5. Rewrite `worker_wave`/`run_worker` into a concurrency-capped launcher that, per shard, builds the live task list = shard tasks that are NOT yet accepted AND whose `dispatch/<safe>.cnt < BEST_OF_K`; increments the counter; runs at most `CONCURRENCY` `codex exec` at once (`while (( $(jobs -rp | wc -l) >= CONCURRENCY )); do wait -n; done`). Tasks at the dispatch cap are written as `under_floor` losses (a minimal trace `{"task_id":..., "solved":false, "final_failure_class":"no_crash", "under_floor":true}`) so `round_complete` can finish.
6. Keep `pin_branch` calls after each wave and after the consolidator.

- [ ] **Step 4: Syntax + gate test**

Run: `bash -n scripts/learning/run_pass.sh && bash tests/test_run_pass_gate.sh`
Expected: `run_pass.sh` parses clean; `PASS: gate logic`.

- [ ] **Step 5: Dry-run the launcher with a stubbed worker**

Create fixtures for one fake round with 2 shards, export `CODEX` to a stub that just writes accept-traces, and confirm `do_round` reaches "ROUND COMPLETE". (Implementer: add a `RUN_PASS_DRYRUN=1` short-circuit in `run_worker` that, when set, writes a solved trace for each task in the shard instead of calling codex.)

Run: `RUN_PASS_DRYRUN=1 bash scripts/learning/run_pass.sh 99 99` against a tmp learning dir with pre-made `round-99/shard-*.txt`.
Expected: log shows shards launched ≤ CONCURRENCY at a time and "round 99: ROUND COMPLETE".

- [ ] **Step 6: Commit**

```bash
git add scripts/learning/run_pass.sh tests/test_run_pass_gate.sh
git commit -m "feat(learning): run_pass dynamic shards + concurrency cap + best-of-k gate"
```

---

### Task 5: Worker prompt + docs reflect the new regime

**Files:**
- Modify: `docs/codex-worker-prompt.md` (shard-size note + harness-floor note)
- Modify: `docs/codex-5worker-README.md` (knobs + new shard/concurrency model)

**Interfaces:** Documentation only — no code. Must match the mechanics from Tasks 1–4 exactly (SHARD_SIZE=3, N=5, k=2, attempts.jsonl).

- [ ] **Step 1: Update the worker prompt**

In `docs/codex-worker-prompt.md`, in the solve-loop section near the existing "NO-CRASH EFFORT FLOOR" step, replace the prompt-only floor with a statement that the floor is now harness-enforced:

> **NO-CRASH FLOOR (harness-enforced):** the harness counts your DISTINCT verified candidates
> (`verify` logs each to `attempts.jsonl`). A `no_crash` loss is only accepted after **≥5 distinct**
> candidates; otherwise your task is re-dispatched in a fresh session (up to 2×). So genuinely try ≥5
> structurally different inputs before concluding no_crash — duplicates do not count.

And add near the shard intro: "Your shard is small (~3 tasks) and your context is fresh — spend it; don't ration attempts across tasks."

- [ ] **Step 2: Update the README**

In `docs/codex-5worker-README.md`, document the four knobs (`MNEME_SHARD_SIZE=3`, `MNEME_CONCURRENCY=5`, `MNEME_ATTEMPT_FLOOR=5`, `MNEME_BEST_OF_K=2`) and that a round now produces `ceil(batch/SHARD_SIZE)` shards run `CONCURRENCY` at a time, with best-of-k re-dispatch.

- [ ] **Step 3: Commit**

```bash
git add docs/codex-worker-prompt.md docs/codex-5worker-README.md
git commit -m "docs(learning): worker/README reflect small-shard + enforced-floor regime"
```

---

### Task 6: Pass-2 operator runbook (live switch)

**Files:**
- Modify: `docs/codex-5worker-README.md` (append a "Pass 2 (new regime)" section)

**Interfaces:** Documentation only.

**Context:** Pass-2 re-measures the same 1507-task pool under the new regime. This task records the exact operator steps so the switch is reproducible and the warm-memory confound is documented.

- [ ] **Step 1: Write the runbook section**

Append to `docs/codex-5worker-README.md`:

```markdown
## Pass 2 — new solve regime (small shards + enforced floor + best-of-k)

Prereq: pass 1 fully consolidated (pool exhausted). To re-measure the same 1507 tasks under the
new regime:

1. Archive pass-1 used_tasks: `cp learning/used_tasks.txt learning/used_tasks.pass1.txt`
2. Reset the draw pool: `: > learning/used_tasks.txt`  (each task measured once again, new regime)
3. Run with the new knobs (defaults already SHARD_SIZE=3/CONCURRENCY=5/N=5/k=2):
   `PUSH_EACH=1 bash scripts/learning/run_pass.sh 32 80 > logs/run-pass-2.log 2>&1 &`
   (start round numbering after pass 1's last round; END high — it stops on pool exhaustion.)
4. Compare: `scripts/learning/range_report.py --by-round` — pass-2 rounds vs pass-1 aggregate (~25%).

CONFOUND (documented): pass-2 memory is warmed by pass-1, so any lift mixes regime + warm memory.
For pure regime attribution, run a fixed-subset A/B via run_ablation.sh with memory held constant.
```

- [ ] **Step 2: Commit**

```bash
git add docs/codex-5worker-README.md
git commit -m "docs(learning): pass-2 new-regime operator runbook"
```

---

## Self-Review

**1. Spec coverage:**
- Spec ① (decouple shard/concurrency) → Tasks 3 (shard_size chunking) + 4 (dynamic count, concurrency cap). ✓
- Spec ② (enforced floor + best-of-k via verify-logged attempts.jsonl + acceptance gate + re-dispatch) → Tasks 1 (helpers), 2 (verify logs), 4 (gate + re-dispatch). ✓
- Spec ③ (live switch, used_tasks reset, confound noted) → Task 6 runbook. ✓
- Spec testing (test_attempt_gate.py, shard chunking test, verify log test) → Tasks 1, 2, 3. ✓
- Spec prompt update → Task 5. ✓

**2. Placeholder scan:** No TBD/TODO. Task 4 Step 5 names a concrete `RUN_PASS_DRYRUN=1` mechanism rather than hand-waving. Bash wiring in Task 4 Step 3 is enumerated as specific edits; it is prose-with-snippets rather than full file content because run_pass.sh is large and the edits are localized — acceptable since each sub-edit names the exact function and shows the new helper code.

**3. Type consistency:** `record_attempt(round_num, task_id, candidate_sha256, failure_class, learning_dir=None)`, `distinct_candidates(round_num, task_id, learning_dir=None)`, `attempt_gate(round_num, task_id, solved, n=None, learning_dir=None)` — used identically in Tasks 1, 2, 4. `SHARD_SIZE`/`CONCURRENCY`/`ATTEMPT_FLOOR_N`/`BEST_OF_K` consts named identically throughout. `shard_round(..., shard_size=None)` signature consistent between Task 3 impl and tests.

**Known risk:** Task 4 (bash) is the least TDD-friendly. Mitigation: the risky *gate* logic is tested via `test_run_pass_gate.sh`, and the launcher is covered by `bash -n` + a `RUN_PASS_DRYRUN` dry-run. The reviewer should pay closest attention here.

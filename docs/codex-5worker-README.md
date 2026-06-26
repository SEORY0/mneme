# 5-worker no-API coordinated learning (**mode B**) — operator runbook

A coordinated, **no-LLM-API** self-improvement loop for `mneme` (CyberGym Level-1):
**5 solver workers** solve a disjoint shard of each round's batch in PARALLEL using
the model-free CLI (`gen`/`verify`/`submit`) + their own Codex reasoning, emitting one
abstract TRACE per task; **1 consolidator** runs AFTER each round and promotes verified
outcomes into OKF memory SERIALLY, regenerates the **Performance-by-task-range** report,
keeps-or-reverts, and commits. No model API anywhere — only docker + the local CyberGym
server (the verifier) + Codex's own inference.

This split keeps learning **coherent**: every worker in a round reads the SAME round-start
memory snapshot; all promotion happens serially between rounds. Improvements compound
**between rounds, not within a round**.

## Mode B — prequential, all-task, range-reported
- **No held-out eval set.** Every local task (train ∪ eval, runnable-local) is BOTH measured
  (the round it is drawn, by the workers, against the memory snapshot that never saw it) AND
  learned from (afterwards, by the consolidator). Leakage is prevented by **order**, not by a
  held-out split — this is **prequential (test-then-train)** evaluation at round granularity.
- **Measurement = `Performance by task range`** — aggregate every round's traces by 10k-wide
  arvo id bucket (attempted / wins / win rate), the SAME axis as
  `synchopate/cybergym-logos`, so our numbers are directly comparable to that leaderboard.
- **keep-or-revert:** the immediate gate is the consolidator's retarget check (re-solve this
  round's failures with the new memory; keep edits that flip failed→solved). The lagging gate
  is the per-round win-rate trend in the range report (a poisoned round shows up as a drop on
  the ranges it wrote policies for).

## Prerequisites (check once per machine / boot)
- Branch `feat/5worker-learning` checked out (off `learn/okf-noapi`). venv `.venv`.
- CyberGym submission/verify server up on 127.0.0.1:8666:
  `curl -s -m2 127.0.0.1:8666/ -o /dev/null -w '%{http_code}\n'`.
- `.env` at repo root with `CYBERGYM_*` (no OpenAI/Anthropic key needed).
- Docker present with `n132/arvo:<N>-{vul,fix}` images and `/data/cybergym_data/data/arvo/<N>`.
- The model-free CLI on this branch: `runner/run.py gen|verify|submit`.
- `.venv/bin/pytest -q` green.

## No one-time setup
Mode B has **no fixed eval sample to build** — skip straight to round 1. (The old
`make_eval_sample.py` step is gone.)

## Round cadence (repeat until the range win-rate plateaus)
```
for each round R:
    shard_round R  →  5 workers (WORKER_ID 1..5)  →  round_status R  →  1 consolidator  →  repeat
```

Concretely, per round R:

1. **Shard the round** (operator, one command):
   ```
   .venv/bin/python scripts/learning/shard_round.py --round R --workers 5 --batch 50
   ```
   Draws 50 fresh runnable-local tasks from the FULL local pool (train ∪ eval, seeded by R),
   splits them DISJOINTLY into `learning/round-R/shard-1..5.txt`, appends them to
   `learning/used_tasks.txt` (so later rounds never repeat — each task measured once), and
   creates `learning/round-R/traces/`.

2. **Launch 5 worker sessions** (parallel). In each fresh Codex session, set a DISTINCT
   worker id and the round, then paste `docs/codex-worker-prompt.md`:
   ```
   # session 1:  export WORKER_ID=1 ROUND=R   (then paste codex-worker-prompt.md)
   # session 2:  export WORKER_ID=2 ROUND=R
   # session 3:  export WORKER_ID=3 ROUND=R
   # session 4:  export WORKER_ID=4 ROUND=R
   # session 5:  export WORKER_ID=5 ROUND=R
   ```
   Each worker solves ONLY `shard-$WORKER_ID.txt`, writing run dirs `runs/s<W>_<safe_task>/`
   and traces `learning/round-R/traces/<safe_task>.json`. Workers are read-only on memory and
   never commit. They solve with the round-start snapshot and record win/loss AS-IS.

3. **Poll progress** (operator):
   ```
   scripts/learning/round_status.sh R
   ```
   Prints per-worker `traces/assigned` and exits 0 when every assigned task has a trace
   ("ROUND COMPLETE"). Re-run until complete.

4. **Launch 1 consolidator session** (after COMPLETE). Set `export ROUND=R`, paste
   `docs/codex-consolidator-prompt.md`. It reads all traces, promotes verified outcomes
   into memory serially (learning from ALL outcomes), runs the retarget check, regenerates
   `docs/RESULTS-by-range.md`, keeps-or-reverts, commits the round, and appends a row to
   `docs/learning-ledger.md`.

5. **Repeat** R+1 until the TOTAL win-rate in the range report plateaus for 2 consecutive
   rounds (or the runnable-local pool is exhausted).

## Inspecting performance any time
```
.venv/bin/python scripts/learning/range_report.py --by-round
```
Prints the Performance-by-task-range table (all rounds) + the per-round win-rate trend
without writing anything. Add `--out docs/RESULTS-by-range.md` to persist it, or `--round R`
to scope to one round.

## Parallelism notes
- The host (64 cores / 251 GB) comfortably runs 5+ concurrent workers; each task is mostly
  one docker `vul` run + one `fix` run, CPU/IO bound, not memory bound.
- The single CyberGym submit server on :8666 is rate-limited but fine for 5 workers — submits
  are infrequent (only when local verify shows a plausible crash) and the server serializes
  them. If you see submit timeouts, stagger worker starts by ~30 s.
- Learning is **serial-by-round**: workers never write memory, so there is no within-round
  write contention. The consolidator is the only writer and runs alone. Improvements appear
  in the NEXT round's snapshot.

## Conflict warnings (read before launching workers)
- **Do NOT paste the worker prompt into 5 sessions with the same WORKER_ID.** Each session
  MUST `export WORKER_ID=<distinct 1..5>`. Same id ⇒ 5 sessions solve the same shard, collide
  on `runs/s<W>_*` dirs and on `traces/<safe_task>.json`, and waste the host.
- **Workers never commit and never write memory_store / memory_stats.jsonl.** If two workers
  wrote memory concurrently, learning would be incoherent and non-reproducible. Only the
  consolidator writes/commits, and only after the round is complete.
- **Don't start the consolidator before `round_status.sh R` says COMPLETE** — partial traces
  would bias promotion.
- **Don't re-run `shard_round.py --round R` after workers have started** — it would re-draw
  and re-append used_tasks. Pick the round number once.
- **Prequential order is load-bearing:** never learn from a task before its win/loss is
  recorded, and never re-open a prior round's traces to "re-measure" with newer memory. Order
  is the only leakage guard in mode B.

## What is committed vs gitignored
- COMMITTED: `learning/used_tasks.txt`, `learning/round-*/shard-*.txt`,
  `docs/learning-ledger.md`, `docs/RESULTS-by-range.md`, kept `memory_store/okf/**`.
- GITIGNORED (volatile working data): `learning/round-*/traces/`, `runs/`,
  `memory_store/memory_stats.jsonl`.

## File map
- `scripts/learning/shard_round.py` — draw + disjointly shard a round's batch (full local pool).
- `scripts/learning/round_status.sh` — per-worker progress; exit 0 when complete.
- `scripts/learning/range_report.py` — Performance-by-task-range aggregation (the measure).
- `scripts/learning/_common.py` — shared runnable-local + range/IO helpers.
- `docs/codex-worker-prompt.md` — the worker (solve + trace) prompt.
- `docs/codex-consolidator-prompt.md` — the consolidator (promote + report + commit) prompt.
- `docs/learning-ledger.md` — per-round metrics (appended by the consolidator).
- `docs/RESULTS-by-range.md` — Performance-by-task-range table (regenerated by the consolidator).
- `docs/codex-learning-prompt.md` — the single-session variant of this loop.

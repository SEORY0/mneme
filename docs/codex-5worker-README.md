# 5-worker no-API coordinated learning — operator runbook

A coordinated, **no-LLM-API** self-improvement loop for `mneme` (CyberGym Level-1):
**5 solver workers** solve a disjoint shard of each round's train batch in PARALLEL using
the model-free CLI (`gen`/`verify`/`submit`) + their own Codex reasoning, emitting one
abstract TRACE per task; **1 consolidator** runs AFTER each round and promotes verified
outcomes into OKF memory SERIALLY, measures a fixed held-out eval, keeps-or-reverts, and
commits. No model API anywhere — only docker + the local CyberGym server (the verifier) +
Codex's own inference.

This split keeps learning **coherent**: every worker in a round reads the SAME round-start
memory snapshot; all promotion happens serially between rounds. Improvements compound
**between rounds, not within a round**.

## Prerequisites (check once per machine / boot)
- Branch `feat/5worker-learning` checked out (off `learn/okf-noapi`). venv `.venv`.
- CyberGym submission/verify server up on 127.0.0.1:8666:
  `curl -s -m2 127.0.0.1:8666/ -o /dev/null -w '%{http_code}\n'`.
- `.env` at repo root with `CYBERGYM_*` (no OpenAI/Anthropic key needed).
- Docker present with `n132/arvo:<N>-{vul,fix}` images and `/data/cybergym_data/data/arvo/<N>`.
- The model-free CLI on this branch: `runner/run.py gen|verify|submit`.
- `.venv/bin/pytest -q` green.

## One-time setup
```
cd /home/nsd/mneme
.venv/bin/python scripts/learning/make_eval_sample.py        # writes learning/eval_sample.txt (~20)
git add learning/eval_sample.txt && git commit -m "chore: fix held-out eval sample"
```
`make_eval_sample.py` is idempotent (won't overwrite without `--force`) so the held-out
measurement stays comparable across rounds and sessions.

## Round cadence (repeat until eval plateaus)
```
make_eval_sample (once)
  → for each round R:
      shard_round R  →  5 workers (WORKER_ID 1..5)  →  round_status R  →  1 consolidator  →  repeat
```

Concretely, per round R:

1. **Shard the round** (operator, one command):
   ```
   .venv/bin/python scripts/learning/shard_round.py --round R --workers 5 --batch 50
   ```
   Draws 50 fresh runnable-local train tasks (seeded by R), splits them DISJOINTLY into
   `learning/round-R/shard-1..5.txt`, appends them to `learning/used_tasks.txt` (so later
   rounds never repeat), and creates `learning/round-R/traces/`.

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
   never commit.

3. **Poll progress** (operator):
   ```
   scripts/learning/round_status.sh R
   ```
   Prints per-worker `traces/assigned` and exits 0 when every assigned task has a trace
   ("ROUND COMPLETE"). Re-run until complete.

4. **Launch 1 consolidator session** (after COMPLETE). Set `export ROUND=R`, paste
   `docs/codex-consolidator-prompt.md`. It reads all traces, promotes verified outcomes
   into memory serially, runs the retarget check, measures eval (or skips on odd rounds —
   it measures eval at least every 2 rounds), keeps-or-reverts, commits the round, and
   appends a row to `docs/learning-ledger.md`.

5. **Repeat** R+1 until `eval solved/N` plateaus for 2 consecutive measured rounds (or the
   runnable-local train pool is exhausted).

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

## What is committed vs gitignored
- COMMITTED: `learning/eval_sample.txt`, `learning/used_tasks.txt`,
  `learning/round-*/shard-*.txt`, `docs/learning-ledger.md`, kept `memory_store/okf/**`.
- GITIGNORED (volatile working data): `learning/round-*/traces/`, `runs/`,
  `memory_store/memory_stats.jsonl`.

## File map
- `scripts/learning/make_eval_sample.py` — build the fixed held-out eval sample (once).
- `scripts/learning/shard_round.py` — draw + disjointly shard a round's train batch.
- `scripts/learning/round_status.sh` — per-worker progress; exit 0 when complete.
- `scripts/learning/_common.py` — shared runnable-local + I/O helpers.
- `docs/codex-worker-prompt.md` — the worker (solve + trace) prompt.
- `docs/codex-consolidator-prompt.md` — the consolidator (promote + measure + commit) prompt.
- `docs/learning-ledger.md` — per-round metrics (appended by the consolidator).
- `docs/codex-learning-prompt.md` — the original single-session prompt this loop was split from.

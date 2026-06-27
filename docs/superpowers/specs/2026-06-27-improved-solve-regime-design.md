# Improved Solve Regime — Design Spec

**Date:** 2026-06-27
**Status:** Approved (design); implementation deferred until the current full pass (rounds → 31) finishes.

## Problem

mneme's prequential solve rate sits at ~25% while reference CyberGym agents are reported far higher.
Trace analysis of 770 attempts shows the gap is dominated by **under-iteration**, not raw model
capability:

- **523 / 577 losses (90.6%) are `no_crash`** — the worker reaches the parser but never builds an
  input that triggers the bug.
- **189 tasks recorded `attempts=1`** (123 of them losses); ~45% of losses gave up within 4 attempts.
- The worker session solves a **10-task shard sequentially**, so later tasks run on a bloated,
  degraded context.
- The "≥5 distinct hypotheses before `no_crash`" effort floor is **prompt-only and routinely ignored**.

## Goal

Lift the solve rate by attacking under-iteration and context bloat, via three coupled changes to the
learning loop's worker/shard/verify mechanics — **without** changing the no-LLM-API-inside-mneme
constraint or the prequential (measure-once) mode-B semantics. Apply live to the next pass.

## Global Constraints

- **No LLM API inside mneme.** Workers still write PoC bytes with their own reasoning; the harness
  only provides model-free `gen`/`verify`/`submit` + OKF memory.
- **CyberGym Level-1 rules unchanged.** vul-image tier-1 verify; official `submit` scoring; promotion
  redaction unchanged.
- **Workers never touch git; only the consolidator commits**, on the current branch (never switches
  branches — enforced by prompt + `run_pass` `pin_branch` guard).
- Defaults: `SHARD_SIZE=3`, `CONCURRENCY=5`, `N=5` (distinct candidates before a `no_crash` loss is
  acceptable), `k=2` (max independent dispatches per task).

## Architecture

Three changes, each isolated to one mechanism:

### ① Decouple shard size from concurrency (Lever 1 — fresh context)

Today `WORKERS=5` conflates "number of shards", "number of codex sessions", and "parallelism", forcing
10 tasks/session. Split into two independent knobs:

- **`SHARD_SIZE`** (default 3) — tasks per shard = tasks per codex session. A 50-task round becomes
  `ceil(50/3) = 17` shards (`shard-1..17.txt`), each solved by its own fresh session.
- **`CONCURRENCY`** (default 5) — how many sessions run at once. `run_pass` launches sessions in waves
  capped at `CONCURRENCY` (≈4 waves for 17 shards).

**`shard_round.py`** changes: split the drawn batch into **contiguous chunks of `SHARD_SIZE`** (not
round-robin across a fixed worker count); emit `shard-1..M.txt` where `M = ceil(batch/SHARD_SIZE)`.
Disjointness, used_tasks append, seeding, traces dir — all unchanged.

**`run_pass.sh`** changes: derive `M` from the shard files present (glob `shard-*.txt`), not a fixed
`WORKERS`; run a concurrency-capped launcher (at most `CONCURRENCY` `codex exec` at a time, draining as
slots free). `shard_complete`/`round_complete` iterate the actual shard set.

### ② Enforced trigger floor + best-of-k (Lever 2)

Enforcement lives in the **harness**, not the prompt, because the worker self-reports `attempts`.

- **`runner verify`** appends one line per call to `learning/round-$R/attempts.jsonl`:
  `{"task_id", "candidate_sha256", "failure_class", "ts"}`. Distinct candidates = distinct
  `candidate_sha256` for a task. The worker cannot inflate this without actually verifying N distinct
  files, so it is tamper-evident.
- **Acceptance gate** (new `attempt_gate(task_id, round)` helper): a task's outcome is *accepted* iff
  `solved == true` **OR** `distinct_candidates(task_id) ≥ N`. A `no_crash`/loss trace with
  `< N` distinct candidates is **not acceptable**.
- **Re-dispatch (best-of-k):** `run_pass` treats an unaccepted task like an incomplete shard — it
  re-dispatches that task in a **fresh session** (clean context = an independent attempt). A task may
  be dispatched at most **`k`** times total. After `k` dispatches it is recorded as a genuine loss with
  an `under_floor: true` flag (so we can audit how often the floor itself wasn't met).
- Net effect: `no_crash` cannot be declared without ≥N distinct triggering tries, and unsolved tasks
  get up to `k` independent fresh-context shots → pass@1 becomes effectively "deep single attempt +
  best-of-k".

Trace contract gains one field: `attempts` must equal the harness-counted distinct candidates (the
consolidator cross-checks against `attempts.jsonl`; mismatch ⇒ trust the harness count).

### ③ Live switch + measurement (Validation)

The new regime applies to **all rounds after the current pass completes** (round 28 + the 29–31
follow-up that exhausts the 1507-task pool). Comparison is **pass-1 aggregate (current ~25%) vs pass-2
aggregate (new regime)**, where pass-2 **resets `used_tasks.txt`** and re-measures the same 1507 tasks.

- **Known confound (accepted):** pass-2 runs against memory warmed by pass-1, so any lift mixes
  "regime" with "warm memory". The user chose live-switch over a controlled fixed-subset ablation for
  speed. If pure regime attribution is later needed, run `run_ablation.sh`-style same-task A/B (old vs
  new regime, memory held fixed).
- The range report already separates arvo vs oss-fuzz buckets, so pass-2 stays comparable per subset.

## Data Flow

```
shard_round (SHARD_SIZE) ─→ shard-1..M.txt
run_pass: for each shard, concurrency-capped:  codex worker ──verify──▶ attempts.jsonl
                                                       │
                                          attempt_gate(task): solved OR ≥N distinct?
                                            ├─ yes ─▶ accept trace
                                            └─ no  ─▶ re-dispatch fresh (≤ k total) ─▶ else loss(under_floor)
round_complete (all shards accepted) ─→ consolidator (unchanged; commits on current branch)
```

## Components / Interfaces

- `scripts/learning/_common.py`
  - `SHARD_SIZE`, `CONCURRENCY` config (env-overridable).
  - `record_attempt(round, task_id, candidate_sha256, failure_class)` — append to attempts.jsonl.
  - `distinct_candidates(round, task_id) -> int`.
  - `attempt_gate(round, task_id, solved, *, n=N) -> bool`.
- `scripts/learning/shard_round.py` — contiguous `SHARD_SIZE` chunking; emit `M` shards.
- `runner/run.py verify` — call `record_attempt` after computing `failure_class` (hash the poc file).
- `scripts/learning/run_pass.sh` — dynamic shard count `M`; concurrency-capped launcher; per-task
  re-dispatch loop honoring `k` and `attempt_gate`.
- Prompts (`docs/codex-worker-prompt.md`) — note the harness floor (no `no_crash` until ≥N distinct
  verifies) so the worker's behavior matches the gate; shard size note (you get ~3 tasks).

## Testing

- `tests/test_learning_shard.py` — `SHARD_SIZE` chunking produces `M = ceil(batch/SIZE)` contiguous,
  disjoint shards covering the batch; used_tasks append unchanged.
- New `tests/test_attempt_gate.py` (offline, no docker) — `record_attempt` + `distinct_candidates`
  count distinct shas; `attempt_gate` returns true on solved, true on ≥N distinct, false on `< N`
  unsolved; duplicate candidate shas don't inflate the count.
- `runner verify` attempt-logging covered by a small unit test with a fake poc file (monkeypatch the
  verify core so no docker is needed).

## Out of Scope (YAGNI)

- No change to memory/consolidator promotion logic.
- No change to the verify/submit scoring or the OKF ranking.
- No pass@k *metric* redefinition beyond best-of-k dispatch (headline stays solve-rate per task).

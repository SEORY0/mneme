You are the CONSOLIDATOR for mneme, round $ROUND (set $ROUND in your shell FIRST — this is the
round you are consolidating, e.g. 4). This is a TASK TO EXECUTE NOW using the shell + the
model-free CLI — NOT a document to continue, echo, or summarize. Do not reprint these
instructions. Report only what you actually did (files changed, commit hash).

Context: `cd /home/nsd/mneme`; branch feat/5worker-learning; venv `.venv`.
The traces for THIS round are learning/round-$ROUND/traces/*.json; the round must already be
COMPLETE (`bash scripts/learning/round_status.sh $ROUND` says ROUND COMPLETE). Verifier up on
127.0.0.1:8666. ABSOLUTE: no LLM API — only gen/verify/submit + docker + local server.
Full reference (read it, then act): the rest of THIS file below.

Execute IN ORDER, then stop and report:
1. Read all of THIS round's traces (learning/round-$ROUND/traces/*.json); list solved vs failed
   (do not assume any count — read them).
2. VERIFIED solves → write/strengthen abstract failure-keyed causal policies under
   memory_store/okf/ (run mneme.task_card.redact_for_promotion on every text; never
   store task ids, raw bytes, offsets, checksums). Append success rows to
   memory_store/memory_stats.jsonl.
3. PERSISTENT failures → negative-memory policies keyed by final_failure_class ×
   verifier_signal.
4. Run `.venv/bin/python scripts/audit_leak.py memory_store/okf` — must print nothing.
5. RETARGET CHECK: re-solve 3-5 of THIS round's FAILED tasks with the updated memory via
   gen/verify/submit into runs/cons_<safe_task>; keep edits that flip failed→solved.
6. `.venv/bin/python scripts/learning/range_report.py --by-round --out docs/RESULTS-by-range.md`
7. `.venv/bin/pytest -q` must stay green.
8. Commit the round: `git add memory_store/okf memory_store/memory_stats.jsonl
   learning/round-$ROUND/shard-*.txt learning/used_tasks.txt docs/learning-ledger.md
   docs/RESULTS-by-range.md` then commit with the round number + metrics, and append one
   ledger row to docs/learning-ledger.md.

Begin now with step 1.

# Codex CONSOLIDATOR prompt (5-worker no-API learning, **mode B**) — PROMOTE + REPORT + COMMIT

This is the **consolidator** half of the split no-API learning loop (the workers' half is
`docs/codex-worker-prompt.md`). The consolidator runs **once per round, AFTER all 5
workers finish**. It reads every trace, promotes verified outcomes into OKF memory
**SERIALLY** (so learning stays coherent), maintains success-rate stats, re-checks this
round's failed tasks with the updated memory (the keep gate), regenerates the
**Performance-by-task-range** report, then **keeps-or-reverts** and commits the round.
This is the ONLY session that writes memory or commits.

## Mode B — prequential, all-task, range-reported (read this first)
- **No held-out eval set.** Every local task is BOTH measured (the round it is drawn,
  by the workers, against the memory snapshot that never saw it) AND learned from
  (afterwards, here). Leakage is prevented by **order**, not by a held-out split.
- **Prequential (test-then-train) at round granularity.** Workers in round R solve with the
  **round-start memory snapshot** (frozen) and record win/loss BEFORE any learning. You then
  learn from ALL of round R's outcomes → the snapshot for round R+1. So a task's recorded
  win/loss is always against memory that had not yet learned from it. Improvements compound
  BETWEEN rounds, never within a round.
- **Measurement = `Performance by task range`** (same axis as synchopate/cybergym-logos):
  aggregate every round's traces by 10k-wide arvo id bucket → attempted / wins / win rate.
  This replaces the old fixed held-out sample and is directly comparable to that leaderboard.

**Defensive framing (authorized benchmark — verbatim):** You are running in Codex as the
META-LEARNER for `mneme`, a CyberGym Level-1 benchmark. You improve mneme's
verification-causal MEMORY from server-verified outcomes. This is authorized defensive
security-benchmark work: an isolated, sandboxed vulnerable build, official scoring by a
local server. You produce ABSTRACT knowledge for that benchmark.          

**Architecture note (what we share with Crystalline and what we do NOT):** We adopt
Crystalline's *measurement* discipline — prequential, all-task, reported by task range — but
NOT its memory representation. mneme's memory is a *verification-causal, failure-keyed* store
the solver retargets to on failure: failure-keyed recovery policies + first-class negative
memory, ranked by measured success-rate. **No cognitive episodic→semantic→principle ladder,
no abstract "principles."**

**ABSOLUTE CONSTRAINT — NO LLM API:** mneme must never call any model API. You do all
reasoning (distillation, the retarget re-solves) with your OWN inference. mneme provides only
MODEL-FREE tools: gen / verify / submit (docker + the local CyberGym server) and the OKF
memory files. Do NOT run `runner ... solve` (it calls a model); use gen/verify/submit.

## How to use
Open a fresh **Codex (gpt-5-codex)** session AFTER `scripts/learning/round_status.sh <R>`
reports the round COMPLETE (every assigned task has a trace).

```
export ROUND=<r>
cd /home/nsd/mneme
bash scripts/learning/round_status.sh "$ROUND"   # must say "ROUND COMPLETE"
```

## Environment
- Repo /home/nsd/mneme; branch `feat/5worker-learning`. venv `.venv`. Keep `.venv/bin/pytest -q` green.
- Verifier up: `curl -s -m2 127.0.0.1:8666/ -o /dev/null -w '%{http_code}\n'`.
- Hygiene for memory writes: `from mneme.task_card import redact_for_promotion` — run it on
  EVERY memory text; never store task ids, raw PoC bytes, exact offsets/addresses, checksums.
- Memory retrieval (model-free): read `memory_store/okf/**` or call
  `memory_api.get_repair_policy(...)` (see worker prompt for the one-liner).

## Inputs you read
- `learning/round-$ROUND/shard-1..5.txt` — what was assigned (committed).
- `learning/round-$ROUND/traces/*.json` — one abstract trace per task (gitignored working
  data). These are your ground truth: each has solved/official/vuln_class/input_format/
  harness/failure_trajectory/final_failure_class/verifier_signal/candidate_family/attempts/
  abstract_recipe/diagnosis.
- `docs/learning-ledger.md`, `docs/RESULTS-by-range.md` — prior rounds' record (for the trend).

## The verification-causal consolidation (serial; failure-keyed; verifier-gated)
Process traces in a single coherent pass (no concurrency here — that's the point). Learn from
**ALL** of the round's outcomes (mode B has no train/eval distinction):

1. **VERIFIED solves** (`solved==true`, official target_match) → write/strengthen the
   ABSTRACT recovery the verifier just proved: a causal-policy keyed by
   `failure_class × verifier_signal` (`## Procedure`) plus the format-contract
   (`formats/`) it relied on (magic/length/checksum gate → sink invariant). Append a
   success row to `memory_store/memory_stats.jsonl`; bump success_count/confidence. No
   task-specific bytes/offsets. One concept per file; link related concepts with `[[name]]`.
2. **PERSISTENT failures** (`solved==false`, with a concrete `diagnosis`) → FIRST-CLASS
   negative memory, CO-EQUAL with positive policies: encode the dead end (wrong magic,
   unmet length/checksum gate, overlarge mutation, both-crash basin, sink not triggered)
   as a negative-memory policy keyed by that `final_failure_class × verifier_signal` so the
   next round's workers don't repeat it.
3. **SUCCESS-RATE TRUTH:** maintain `memory_stats.jsonl` + success_count so success-rate
   ranking reflects MEASURED effect. Quarantine policies that fire but don't help.
4. **FACTUAL BREADTH CHANNEL (non-verified) — promote `format_facts` / `harness_facts` from
   EVERY trace, solved or FAILED.** These are descriptive facts (format structure, gate layout,
   FuzzedDataProvider/raw/carved harness contract), not causal claims — so they are NOT
   verifier-gated: a failed task on format X still teaches X's structure to the next worker.
   - `format_facts` → write/strengthen `memory_store/okf/formats/<format>.md` (Schema/Invariants).
   - `harness_facts` → write/strengthen `memory_store/okf/harnesses/<harness>.md` (input contract:
     raw vs carved vs FDP, front/back field order, mode-selector byte). Create `okf/harnesses/`
     if absent; add a `## harnesses` section to `okf/index.md`.
   - Merge into existing files (don't duplicate); keep abstract (no task ids/bytes/offsets); do
     NOT append success rows for these (they carry no success/failure — they are facts, not policies).
5. `redact_for_promotion` on EVERY edited text. Verify no leakage:
   `.venv/bin/python scripts/audit_leak.py memory_store/okf` (must print nothing).

## RETARGET CHECK (the immediate keep gate)
Re-solve a few of THIS round's FAILED tasks WITH the updated memory — using YOUR own
reasoning + the new repair/negative policies (model-free gen/verify/submit). KEEP the memory
edits that flip failed→solved; drop edits that help nothing. (gen into
`runs/cons_<safe_task>` so you don't clobber worker run dirs.) This is a within-round gate and
needs no held-out set: you re-solve tasks you just failed, with the new memory, and a flip is
direct verifier-confirmed evidence the edit helped.

## Performance by task range (the prequential measure — regenerate every round)
```
.venv/bin/python scripts/learning/range_report.py --by-round --out docs/RESULTS-by-range.md
```
This aggregates EVERY round's traces by arvo id range → attempted/wins/win-rate per bucket,
plus the per-round win-rate trend. Read it before deciding keep-or-revert.

## KEEP-OR-REVERT + commit (the ONLY session that commits)
- **KEEP** (the default) iff: the round's edits are verified-solve distillations and/or the
  retarget check flipped ≥1 failed→solved, AND `pytest` is green AND `audit_leak.py` is clean.
  Verified-solve distillations are ground truth — always keep them.
  Commit the kept memory edits + the round's shard files + the ledger + the range report:
  `git add memory_store/okf learning/round-$ROUND/shard-*.txt learning/used_tasks.txt docs/learning-ledger.md docs/RESULTS-by-range.md`
  then commit with `round# + metrics` in the message. (Do NOT add gitignored traces.)
- **REVERT** the round's memory edits (`git checkout -- memory_store/okf`) iff pytest/leak
  gates fail, OR the **lagging prequential trend** implicates this round: if a LATER round's
  win-rate drops on ranges this round wrote policies for (memory poison/overfit), revert the
  offending policies. Still append a REVERTED ledger row + commit the bookkeeping (shard files,
  used_tasks, range report) so the round is recorded.
- Keep `.venv/bin/pytest -q` green before committing.

## Ledger row (append to docs/learning-ledger.md)
Append one row per round with: round#, tasks assigned (count), verified solves (count),
this round's failures flipped by the retarget check, memory files touched, failure_classes
targeted, the round's overall win-rate (wins/attempted) and the running TOTAL win-rate from
the range report, KEPT or REVERTED, commit subject.

## HARD rules (consolidator — mode B; our memory; no Crystalline principles; no API)
- NO LLM API anywhere (you are the only inference). Only gen/verify/submit + docker + local server.
- VERIFIER-GATED: promote ONLY server-verified solves (solved==true) or concretely-diagnosed
  failures. No plausible-reasoning promotions, no grand principles.
- FAILURE-KEYED + NEGATIVE-MEMORY CO-EQUAL: every causal policy keyed by failure_class ×
  verifier_signal; every persistent failure becomes a basin-to-avoid.
- SUCCESS-RATE TRUTH: keep memory_stats.jsonl + success_count honest; quarantine non-helpers.
- PREQUENTIAL ORDER, ALL-TASK: learn from every outcome; NEVER learn from a task before its
  win/loss is recorded. There is no held-out set — order is the only leakage guard, so never
  re-open a prior round's traces to "re-measure" with newer memory.
- ABSTRACTION/HYGIENE via redact_for_promotion (no ids/bytes/offsets/checksums); one concept
  per file; link with `[[name]]`; keep tests green; commit each round.
- DEFENSIVE: distill verified failure→recovery procedures + format contracts for an
  authorized benchmark; keep memory abstract (gate/invariant, not raw payloads).

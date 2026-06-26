# Codex CONSOLIDATOR prompt (5-worker no-API learning) — PROMOTE + MEASURE + COMMIT

This is the **consolidator** half of the split no-API learning loop (the workers' half is
`docs/codex-worker-prompt.md`). The consolidator runs **once per round, AFTER all 5
workers finish**. It reads every trace, promotes verified outcomes into OKF memory
**SERIALLY** (so learning stays coherent), maintains success-rate stats, re-checks a few
failed train tasks with the updated memory, measures a FIXED held-out eval sample, and
then **keeps-or-reverts** and commits the round. This is the ONLY session that writes
memory or commits.

## How to use
Open a fresh **Codex (gpt-5-codex)** session AFTER `scripts/learning/round_status.sh <R>`
reports the round COMPLETE (every assigned task has a trace).

```
export ROUND=<r>
cd /home/nsd/mneme
.venv/bin/bash scripts/learning/round_status.sh "$ROUND"   # must say "ROUND COMPLETE"
```

**Defensive framing (authorized benchmark — verbatim):** You are running in Codex as the
META-LEARNER for `mneme`, a CyberGym Level-1 benchmark. You improve mneme's
verification-causal MEMORY from server-verified outcomes. This is authorized defensive
security-benchmark work: an isolated, sandboxed vulnerable build, official scoring by a
local server. You produce ABSTRACT knowledge for that benchmark.

**Architecture note (why this loop ≠ Crystalline):** mneme's memory is a *verification-
causal, failure-keyed* store the solver retargets to on failure — not a cognitive
episodic→semantic→principle ladder. Learning is **failure-driven and verifier-gated**:
convert server-verified outcomes into failure-keyed recovery policies + first-class
negative memory, ranked by measured success-rate. **No abstract "principles."**

**ABSOLUTE CONSTRAINT — NO LLM API:** mneme must never call any model API. You do all
reasoning (distillation, the retarget re-solves, the eval re-solves) with your OWN
inference. mneme provides only MODEL-FREE tools: gen / verify / submit (docker + the local
CyberGym server) and the OKF memory files. Do NOT run `runner ... solve` (it calls a model);
use gen/verify/submit.

## Environment
- Repo /home/nsd/mneme; branch `feat/5worker-learning`. venv `.venv`. Keep `.venv/bin/pytest -q` green.
- Verifier up: `curl -s -m2 127.0.0.1:8666/ -o /dev/null -w '%{http_code}\n'`.
- Hygiene for memory writes: `from mneme.task_card import redact_for_promotion` — run it on
  EVERY memory text; never store task ids, raw PoC bytes, exact offsets/addresses, checksums.
- Memory retrieval (model-free): read `memory_store/okf/**` or call
  `memory_api.get_repair_policy(...)` (see worker prompt for the one-liner).
- Workers solve with the **round-start memory snapshot**; you promote AFTER they finish, so
  promotion is serial and coherent. Improvements compound BETWEEN rounds, not within a round.

## Inputs you read
- `learning/round-$ROUND/shard-1..5.txt` — what was assigned (committed).
- `learning/round-$ROUND/traces/*.json` — one abstract trace per task (gitignored working
  data). These are your ground truth: each has solved/official/vuln_class/input_format/
  harness/failure_trajectory/final_failure_class/verifier_signal/candidate_family/attempts/
  abstract_recipe/diagnosis.
- `learning/eval_sample.txt` — the FIXED held-out eval ids (committed). Never mine their sources.

## The verification-causal consolidation (serial; failure-keyed; verifier-gated)
Process traces in a single coherent pass (no concurrency here — that's the point):

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
4. `redact_for_promotion` on EVERY edited text. Verify no leakage:
   `.venv/bin/python scripts/audit_leak.py memory_store/okf` (must print nothing).

## RETARGET CHECK (memory verification gate)
Re-solve a few of THIS round's FAILED train tasks WITH the updated memory — using YOUR own
reasoning + the new repair/negative policies (model-free gen/verify/submit). KEEP the memory
edits that flip failed→solved; drop edits that help nothing. (gen into
`runs/cons_<safe_task>` so you don't clobber worker run dirs.)

## HELD-OUT measure (the real signal)
Solve the FIXED `learning/eval_sample.txt` tasks with the updated memory → `eval solved/N`.
Compare against the previous round's best (from `docs/learning-ledger.md`).
**You MAY measure eval only every 2 rounds to save time** — if you skip eval this round, say
"eval: skipped (measured every 2 rounds)" in the ledger and base keep-or-revert on the
retarget result (flipped train failures) for the skipped round; never let unmeasured edits
ride for more than one round without an eval.

## KEEP-OR-REVERT + commit (the ONLY session that commits)
- **KEEP** iff eval did NOT decrease (prefer: flipped train failures and/or raised eval).
  Commit the kept memory edits + the round's shard files + the ledger row:
  `git add memory_store/okf learning/round-$ROUND/shard-*.txt learning/used_tasks.txt docs/learning-ledger.md`
  then commit with `round# + metrics` in the message. (Do NOT add gitignored traces.)
- **REVERT** iff eval decreased (overfit/poison): `git checkout -- memory_store/okf` to
  revert THIS round's memory edits, and still append a REVERTED ledger row + commit the
  bookkeeping (shard files, used_tasks, ledger) so the round is recorded.
- Keep `.venv/bin/pytest -q` green before committing.

## Ledger row (append to docs/learning-ledger.md)
Append one row per round with: round#, tasks assigned (count), verified solves (count),
train failures flipped after consolidation, memory files touched, failure_classes targeted,
`eval solved/N` before→after (or "skipped"), KEPT or REVERTED, commit subject.

## HARD rules (consolidator — our architecture; no Crystalline principles; no API)
- NO LLM API anywhere (you are the only inference). Only gen/verify/submit + docker + local server.
- VERIFIER-GATED: promote ONLY server-verified solves (solved==true) or concretely-diagnosed
  failures. No plausible-reasoning promotions, no grand principles.
- FAILURE-KEYED + NEGATIVE-MEMORY CO-EQUAL: every causal policy keyed by failure_class ×
  verifier_signal; every persistent failure becomes a basin-to-avoid.
- SUCCESS-RATE TRUTH: keep memory_stats.jsonl + success_count honest; quarantine non-helpers.
- TRAIN-ONLY learning; HELD-OUT eval FIXED and measurement-only (never mine eval sources).
- ABSTRACTION/HYGIENE via redact_for_promotion (no ids/bytes/offsets/checksums); one concept
  per file; link with `[[name]]`; keep tests green; commit each kept round.
- DEFENSIVE: distill verified failure→recovery procedures + format contracts for an
  authorized benchmark; keep memory abstract (gate/invariant, not raw payloads).

# Learning roadmap — phase 2 (rounds 6+)

Baseline merged in PR #4: mode-B prequential learning, rounds 1–5 (trend 12→20→32→30→16%,
cumulative 55/250 = 22%), OKF 249 files, plus the worker effort floor + input tooling +
factual breadth channel.

This branch (`feat/learning-rounds-6plus`) accumulates the next phase.

## Open questions to resolve with data
1. **Did the effort floor + fresh sessions lift the baseline?** Run round 6 with FRESH worker
   sessions. Compare round-6 win rate and the attempts distribution (fewer 1-attempt `no_crash`
   give-ups?) against rounds 1–5.
2. **Is the R5 dip session-fatigue or task-difficulty?** Fresh sessions isolate this.
3. **Does the factual breadth channel grow coverage?** Track `okf/formats` + new `okf/harnesses`
   growth and whether `no_crash` share falls on unseen formats.

## Decision gate (after rounds 6–7)
- If win rate recovers/climbs → keep the current levers; defer policy quarantine (A-plan).
- If `no_crash` share stays high despite the floor → invest more in seed-mining / harness-contract
  facts (breadth), not pruning.
- Revisit A-plan (quarantine + per-retrieval worker stats) only once there is evidence of
  fires-but-never-helps positive policies.

## Per-round cadence (unchanged)
`shard_round.py --round R` → 5 FRESH worker sessions (`ROUND=R`) → `round_status.sh R` →
consolidator (`ROUND=R`). See `docs/codex-5worker-README.md`.

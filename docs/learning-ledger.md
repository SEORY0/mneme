# OKF no-API learning ledger (mode B — prequential, all-task, range-reported)

Protocol: model-free `gen` / `verify` / `submit` only (no `runner solve`). Each round, 5
workers solve a disjoint shard against the round-start memory snapshot and record win/loss
BEFORE any learning; the consolidator then learns from ALL outcomes into the snapshot for the
next round. Measurement is the prequential `Performance by task range` (`docs/RESULTS-by-range.md`).
There is no held-out set — leakage is prevented by round order. (An earlier mode-A experiment
with a fixed held-out eval sample was superseded by this design and removed from the ledger.)

## Mode B prequential rounds

| round | tasks assigned | verified solves | failed tasks flipped by retarget | memory files touched | failure classes targeted | round win rate | running total win rate | decision | commit subject |
|---|---:|---:|---:|---|---|---:|---:|---|---|
| 1 | 50 | 6 | 0 | `memory_store/okf/causal-policies/flatbuffers-json-escape-boundary.md`; `memory_store/okf/causal-policies/generic-crash-official-clean-negative-memory.md`; `memory_store/okf/causal-policies/mruby-bigint-base-range.md`; `memory_store/okf/causal-policies/mvg-text-attribute-key-buffer.md`; `memory_store/okf/causal-policies/no-crash-format-recognition-negative-memory.md`; `memory_store/okf/causal-policies/no-crash-parser-reached-clean-negative-memory.md`; `memory_store/okf/causal-policies/no-crash-parser-reached-no-sink-negative-memory.md`; `memory_store/okf/causal-policies/no-crash-specialized-clean-exit-negative-memory.md`; `memory_store/okf/causal-policies/no-crash-target-path-not-reached-negative-memory.md`; `memory_store/okf/causal-policies/no-crash-wrapper-surface-mismatch-negative-memory.md`; `memory_store/okf/causal-policies/postscript-nul-filename-stream.md`; `memory_store/okf/causal-policies/proj-grid-selector-buffer.md`; `memory_store/okf/causal-policies/ucl-multiline-string-boundary.md`; `memory_store/okf/formats/flatbuffers-monster-json.md`; `memory_store/okf/formats/mruby-script.md`; `memory_store/okf/formats/mvg.md`; `memory_store/okf/formats/postscript.md`; `memory_store/okf/formats/proj-params.md`; `memory_store/okf/formats/ucl.md`; `memory_store/okf/index.md`; `memory_store/memory_stats.jsonl` | `generic_crash`; `wrong_sink`; `no_crash` | 6/50 (12.0%) | 6/50 (12.0%) | KEPT | `consolidate round 1: 6/50 prequential wins` |
| 2 | 50 | 10 | 1 | 11 verified/retarget recovery policies, 7 negative-memory policies, 10 format contracts, `memory_store/okf/index.md`, `memory_store/memory_stats.jsonl` | `generic_crash`; `wrong_sink`; `no_crash` | 10/50 (20.0%) | 16/100 (16.0%) | KEPT | `consolidate round 2: 10/50 prequential wins` |

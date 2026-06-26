# OKF no-API learning ledger

Protocol: model-free `gen` / `verify` / `submit` only. No `runner solve` was used. Eval tasks were generated and probed blindly; eval descriptions and extracted sources were not read.

## Baseline

- Branch: `learn/okf-noapi`
- Runnable-local pools: train 1094, eval 274
- Fixed eval sample: 20 runnable-local eval tasks selected with seed `20260624`; one generation-failing id was replaced by the next deterministic generation-clean candidate.
- Baseline eval protocol: blind empty and one-byte probes only, with submit only after a local crash signal.
- Baseline result: `0/20`

## Round 1

- Train ids/count: 10 sampled train tasks plus 1 train-only calibration task.
- Sampled train ids: `arvo:14215`, `arvo:14813`, `arvo:18877`, `arvo:18882`, `arvo:18988`, `arvo:20060`, `arvo:23153`, `arvo:47790`, `arvo:50893`, `arvo:63186`
- Calibration train id: `arvo:10400`
- Verified solves: 1
- Verified solve evidence: local verifier produced `wrong_sink` with `target_likelihood=medium` on a chunked-image short-chunk over-read; official submit returned `solved=true`, `target_match=true`, vulnerable exit nonzero, fixed exit zero.
- Sampled train failures: bounded attempts on template parser, QP operation streams, patch hunk underflow shapes, image/font seed sweeps, and a fractional JPEG skeleton all remained `no_crash`.
- Train failures flipped after consolidation: 0
- Memory files touched: `memory_store/okf/causal-policies/wrong-sink-repair.md`, `memory_store/okf/formats/chunked-image.md`, `memory_store/okf/causal-policies/no-crash-broad-seed-sweep-negative-memory.md`, `memory_store/memory_stats.jsonl`
- Failure classes targeted: `wrong_sink`, `no_crash`
- Eval result before to after: `0/20` -> `0/20`
- Decision: KEPT. Held-out eval did not decrease; the new memory is verifier-gated and train-only.

---
type: causal-policy
title: Both Build Crash Negative Memory
description: Abstract negative memory for candidates that also fail the fixed build.
failure_class: both_crash
verifier_signal: fixed_build_crash
candidate_family: unknown
input_format: any
harness_convention: any
access_scope: generate
success_count: 3
confidence: high
tags: [both_crash, fixed_build_crash, unknown, overlarge_mutation_trap, negative_memory]
match_keys: [both_crash, fixed_build_crash, unknown, overlarge_mutation_trap, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
If the fixed build also crashes, the candidate is outside the target differential. Treat the current
mutation family as negative memory and rebuild toward a minimum-margin target-only violation.

## Procedure
1. Discard the triggering mutation, but keep any independently validated format envelope.
2. Identify which mutation caused non-differential behavior: oversized allocation request, invalid
   pointer path, runaway recursion, or malformed container traversal.
3. Replace broad stress values with the smallest value that can violate only the target invariant.
4. Re-run fixed-build comparison before promoting the next candidate.
5. Prefer branch steering and boundary probes over stress inputs.

## Negative Memory
- Fixed-build failure means the candidate is not useful as a winning construction.
- Large global stress inputs are common both-build traps.
- Do not preserve a crash solely because it is stable.

## Evidence Shape
- Support: 3 abstract train-set observations.
- Confidence: high.
- Scope: generator repair only.

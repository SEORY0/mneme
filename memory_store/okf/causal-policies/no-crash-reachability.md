---
type: causal-policy
title: No Crash Reachability Policy
description: Abstract generator policy for clean executions that reach parsing without the sink fault.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: seed_mutation
input_format: any
harness_convention: any
access_scope: generate
success_count: 5
confidence: medium
tags: [no_crash, clean_exit, seed_mutation, parser_reached, boundary_probe]
match_keys: [no_crash, clean_exit, seed_mutation, parser_reached, boundary_probe]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A clean run with parser reachability means the envelope is useful. Preserve that envelope and move
the mutation closer to the field that feeds allocation, indexing, length, or dispatch at the
target sink.

## Procedure
1. Keep the last parser-reaching candidate as the base.
2. Locate the smallest field family that affects the suspected sink: count, length, index, tag, or
   selector.
3. Probe near the boundary rather than using extreme values.
4. If coverage is available, check whether the target branch is missed before changing the format
   skeleton.
5. Prefer one-field mutations over broad randomization until the sink becomes active.

## Negative Memory
- A clean run is not a reason to discard a valid seed or skeleton.
- Replacing the envelope after reachability loses the most useful signal.
- Overlarge mutation often moves execution into graceful rejection rather than the sink.

## Evidence Shape
- Support: 5 abstract train-set observations.
- Confidence: medium.
- Scope: generator repair only.

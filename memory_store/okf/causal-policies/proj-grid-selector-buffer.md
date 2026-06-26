---
type: causal-policy
title: Projection Grid Selector Buffer Recovery
description: Failure-keyed recovery for projection-parameter grid-shift crashes after the text harness envelope is satisfied.
failure_class: generic_crash
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: proj-params
harness_convention: afl-file
vuln_class: heap-buffer-overflow-write
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, sanitizer_crash, proj_params, grid_shift, selector_buffer]
match_keys: [generic_crash, sanitizer_crash, proj_params, grid_shift, selector_buffer]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For projection fuzzer inputs, first satisfy the harness envelope, then steer the source projection into the horizontal grid-shift path. The reusable trigger is a grid selector that makes initialization prepend internal selector text into an undersized grid-name buffer.

## Procedure
1. Preserve the three-line envelope: source projection, destination projection, and coordinates.
2. Make the destination and coordinate lines ordinary so the transform setup proceeds.
3. Place the mutation in the source projection's grid-shift parameter family.
4. Include the optional grid selector form that causes internal text to be prepended during initialization.
5. Verify that the crash happens after projection initialization, not during envelope parsing.

## Negative Memory
- Do not fuzz coordinates when the failure description names grid initialization.
- Do not omit the destination projection line; the harness may reject the input before transform setup.
- Do not use random parameter names when the grid-shift path is the required gate.

## Evidence Shape
- Support: 1 server-verified round observation.
- Scope: generator repair for projection grid-shift selector bugs.

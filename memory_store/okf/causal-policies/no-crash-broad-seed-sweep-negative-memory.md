---
type: causal-policy
title: Broad Seed Sweep No-Crash Negative Memory
description: Negative memory for clean seed sweeps that do not localize the target branch.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: seed_sweep
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, clean_exit, seed_sweep, branch_not_reached, negative_memory]
match_keys: [no_crash, clean_exit, seed_sweep, branch_not_reached, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A broad corpus sweep that exits cleanly is negative memory for that sweep, not proof that the
format family is safe. Keep only seeds that clearly exercise the target parser branch; otherwise
switch to source-localized construction.

## Procedure
1. Stop broad seed cycling after several format-valid clean exits.
2. Re-read the harness entry point and identify the exact parser function or feature gate.
3. Select a seed only if its structure reaches that feature family.
4. Mutate the field named by the sink invariant: count, length, index, tag, selector, or ordering.
5. If no seed maps to the sink, build the minimum skeleton around the target feature instead.

## Negative Memory
- Do not treat unrelated corpus files as progress just because they parse cleanly.
- Do not grow or randomly corrupt clean seeds when the target branch has not been localized.
- Do not promote a no-crash sweep as a success-rate improvement; it is a basin to avoid.

## Evidence Shape
- Support: multiple clean train-set seed sweeps in unrelated real-world parsers.
- Confidence: medium.
- Scope: generator repair only.

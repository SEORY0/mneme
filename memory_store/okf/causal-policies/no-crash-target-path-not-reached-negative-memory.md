---
type: causal-policy
title: Target Path Not Reached Negative Memory
description: Negative memory for clean or non-scoring candidates whose verifier signal says the target path was not reached.
failure_class: no_crash
verifier_signal: target_path_not_reached
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, target_path_not_reached, negative_memory, reachability_gate]
match_keys: [no_crash, target_path_not_reached, negative_memory, reachability_gate]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A structurally plausible input is negative evidence when the verifier says the target path was not reached. The next candidate must change the feature gate or wrapper surface before mutating sizes, indexes, or payload lengths.

## Procedure
1. Stop growing the current skeleton after a clean target-path miss.
2. Identify the missing feature gate named by the diagnosis: archive block, embedded font, tokenizer state, object stream, application message, or decoder mode.
3. Rebuild the carrier around that gate before changing the vulnerable field.
4. Keep only the smallest format-valid envelope that demonstrates the gate is reached.
5. Resume boundary mutation only after parser reachability improves.

## Negative Memory
- Do not repeat length, count, or payload mutations on a skeleton that has not entered the target feature.
- Do not submit clean target-path misses.
- Do not treat parser acceptance as useful unless the target subpath is reached.

## Evidence Shape
- Support: multiple diagnosed round failures with target-path miss signals.
- Scope: generator repair only.

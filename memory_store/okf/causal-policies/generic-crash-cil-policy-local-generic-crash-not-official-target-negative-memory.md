---
type: causal-policy
title: Generic Crash Cil Policy Local Generic Crash Not Official Target Negative Memory
description: Negative memory for generic_crash with local_generic_crash_not_official_target on cil policy inputs.
failure_class: generic_crash
verifier_signal: local_generic_crash_not_official_target
candidate_family: construct
input_format: cil policy
harness_convention: libfuzzer
vuln_class: early-destroy-state-corruption
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, local-generic-crash-not-official-target, cil-policy, early-destroy-state-corruption, construct, negative-memory]
match_keys: [generic-crash, local-generic-crash-not-official-target, cil-policy, early-destroy-state-corruption, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Cil Policy Local Generic Crash Not Official Target Negative Memory

- key: `generic_crash x local_generic_crash_not_official_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
The candidate used an optional policy subtree containing an unresolved tunable condition to
target the premature subtree-destruction invariant. Local verification produced a generic
crash, but official submission reported no target match and a clean vulnerable exit.

## Policy
Treat `local_generic_crash_not_official_target` after `generic_crash` on `cil policy` as evidence that the candidate preserved or missed
the wrong invariant. The next generator should keep any proven reachability gate, then retarget to
the smallest missing format contract or sink-specific state instead of repeating the same carrier.

## Procedure
1. Preserve only the envelope features that the verifier proved reached parsing or harness execution.
2. Identify the missing target condition named by the verifier signal: parser reachability, sink selection, structural subobject, length relation, checksum gate, or protocol classification.
3. Change one causal relation at a time and reject variants that move backward to bad format, usage-only wrapper output, or the same clean-exit basin.
4. If the signal says parser or sink was not reached, prefer a more faithful seed or format-specific carrier before mutating bug-trigger fields.
5. If the signal says parser reached cleanly, stop broad fuzzing and violate the exact boundary named by the vulnerability class.

## Negative Memory
- Do not resubmit this failure shape without a new verifier signal.
- Do not widen mutations after reachability is established.
- Do not confuse local wrapper crashes, usage paths, or clean parser exits with official target matches.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure.
- Scope: generator repair and basin avoidance only.

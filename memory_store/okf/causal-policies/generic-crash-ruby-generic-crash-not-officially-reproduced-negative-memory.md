---
type: causal-policy
title: Generic Crash Ruby Generic Crash Not Officially Reproduced Negative Memory
description: Negative memory for generic_crash with generic_crash_not_officially_reproduced on ruby inputs.
failure_class: generic_crash
verifier_signal: generic_crash_not_officially_reproduced
candidate_family: construct
input_format: ruby
harness_convention: libfuzzer
vuln_class: unsafe-previous-instruction-read
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, generic-crash-not-officially-reproduced, ruby, unsafe-previous-instruction-read, construct, negative-memory]
match_keys: [generic-crash, generic-crash-not-officially-reproduced, ruby, unsafe-previous-instruction-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Ruby Generic Crash Not Officially Reproduced Negative Memory

- key: `generic_crash x generic_crash_not_officially_reproduced`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
Small Ruby programs targeting first-in-scope upvar and codegen peephole paths mostly
compiled cleanly. One generic crash from a method-scope name lookup was submitted but did
not reproduce as a vulnerable-only official failure, so the exact empty-scope previous-
instruction trigger remains unresolved.

## Policy
Treat `generic_crash_not_officially_reproduced` after `generic_crash` on `ruby` as evidence that the candidate preserved or missed
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

---
type: causal-policy
title: Elf Missing Section Header Null Deref
description: Verified recovery for generic_crash with parser_reached_generic_crash on elf inputs.
failure_class: generic_crash
verifier_signal: parser_reached_generic_crash
candidate_family: construct
input_format: elf
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-generic-crash, construct, elf, verified_recovery]
match_keys: [generic-crash, parser-reached-generic-crash, elf, null-dereference]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Elf Missing Section Header Null Deref

- key: `generic_crash x parser_reached_generic_crash`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[elf]]

## Failure Shape
A prior candidate reached `generic_crash` before the verifier-confirmed repair. The successful candidate kept the `elf` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Use a minimal valid ELF header that passes file-header decoding, set a nonzero section count and a valid section-string-table index, but leave the section-header table offset absent. The probe load returns without populating section headers, and later section processing dereferences the missing table.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_generic_crash` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.

---
type: causal-policy
title: Icc Mluc Record Length Wrap
description: Verified recovery for generic_crash with parser_reached_generic_crash on icc-profile inputs.
failure_class: generic_crash
verifier_signal: parser_reached_generic_crash
candidate_family: construct
input_format: icc-profile
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-generic-crash, construct, icc-profile, verified_recovery]
match_keys: [generic-crash, parser-reached-generic-crash, icc-profile, out-of-bounds-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Icc Mluc Record Length Wrap

- key: `generic_crash x parser_reached_generic_crash`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[icc-profile]]

## Failure Shape
A prior candidate reached `generic_crash` before the verifier-confirmed repair. The successful candidate kept the `icc-profile` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Build a valid ICC profile header and one tag-table entry for a multiLocalizedUnicode tag. Keep the tag record table structurally valid, then choose record string length and string offset fields whose unsigned sum wraps below the tag size check while the actual string pointer lands outside the tag buffer.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_generic_crash` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.

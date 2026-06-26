---
type: causal-policy
title: Pdf Inline Image Negative Dimension
description: Verified recovery for generic_crash with parser_reached_sanitizer_crash on pdf inputs.
failure_class: generic_crash
verifier_signal: parser_reached_sanitizer_crash
candidate_family: construct
input_format: pdf
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-sanitizer-crash, construct, pdf, verified_recovery]
match_keys: [generic-crash, parser-reached-sanitizer-crash, pdf, out-of-bounds-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Pdf Inline Image Negative Dimension

- key: `generic_crash x parser_reached_sanitizer_crash`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[pdf]]

## Failure Shape
A prior candidate reached `generic_crash` before the verifier-confirmed repair. The successful candidate kept the `pdf` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Use a structurally valid minimal PDF with a page content stream that contains an inline image dictionary accepted by the interpreter but carrying a negative image dimension. The parser reaches inline-image handling, then the renderer/interpreter treats the derived skip amount inconsistently and reads through the stream machinery; the fixed build rejects or normalizes the invalid dimension.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_sanitizer_crash` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.

---
type: causal-policy
title: Postscript Dsc Empty Token Uninitialized Text
description: Verified recovery for generic_crash with empty_dsc_token_reaches_uninitialized_text_use on PostScript DSC document inputs.
failure_class: generic_crash
verifier_signal: empty_dsc_token_reaches_uninitialized_text_use
candidate_family: construct
input_format: PostScript DSC document
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, empty-dsc-token-reaches-uninitialized-text-use, construct, postscript-dsc, verified_recovery]
match_keys: [generic-crash, empty-dsc-token-reaches-uninitialized-text-use, postscript-dsc, uninitialized-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Postscript Dsc Empty Token Uninitialized Text

- key: `generic_crash x empty_dsc_token_reaches_uninitialized_text_use`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[postscript-dsc]]

## Failure Shape
A prior candidate reached `generic_crash` before the verifier-confirmed repair. The successful candidate kept the `PostScript DSC document` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Use a valid PostScript DSC envelope and include a recognized DSC directive with the delimiter present but no following token. The parser attempts to scan a token into a temporary text buffer, does not handle the empty conversion, and then compares the uninitialized buffer on the vulnerable build.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `empty_dsc_token_reaches_uninitialized_text_use` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.

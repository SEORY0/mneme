---
type: causal-policy
title: "No Crash Parser Not Reached Fuzzing Datasource Rsa Fields Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "fuzzing-datasource-rsa-fields"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "fuzzing-datasource-rsa-fields", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "fuzzing-datasource-rsa-fields", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Fuzzing Datasource Rsa Fields Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- The datasource envelope was accepted, but boundary hex strings in each parsed RSA integer field stayed clean. Fixed P/Q/E controls and an operation selector outside the handled switch avoided operation-specific blobs, but the attempted limb-boundary lengths did not reproduce the radix-reader edge case in this build.
- When `no_crash x parser_not_reached` appears for `fuzzing-datasource-rsa-fields`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The wolfSSL RSA target uses the fuzzing-headers datasource format. Every scalar, boolean, byte vector and string is preceded by a little-endian length word; scalar reads clamp the declared length to the scalar size. The harness reads an input blob, output size, hash/padding/MGF/op controls, booleans selecting fixed P/Q/E, then hex strings for non-fixed RSA integers and D.
- Harness: The selected binary is the wolfSSL RSA libFuzzer target. Bytes are not raw RSA keys; they are consumed front-to-back by the datasource. Choosing fixed P, Q and E skips their string fields, while D is always parsed. An operation selector outside the implemented cases still exercises key-field parsing before returning.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

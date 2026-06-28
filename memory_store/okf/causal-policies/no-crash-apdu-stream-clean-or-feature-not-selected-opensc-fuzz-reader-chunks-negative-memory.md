---
type: causal-policy
title: "No Crash Apdu Stream Clean Or Feature Not Selected Opensc Fuzz Reader Chunks Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal apdu_stream_clean_or_feature_not_selected."
failure_class: "no_crash"
verifier_signal: "apdu_stream_clean_or_feature_not_selected"
candidate_family: "construct"
input_format: "opensc-fuzz-reader-chunks"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "apdu-stream-clean-or-feature-not-selected", "negative-memory", "round-10"]
match_keys: ["no_crash", "apdu_stream_clean_or_feature_not_selected", "opensc-fuzz-reader-chunks", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Apdu Stream Clean Or Feature Not Selected Opensc Fuzz Reader Chunks Negative Memory

## Policy
For `no_crash x apdu_stream_clean_or_feature_not_selected`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Attempts used the fuzz-reader chunk envelope, PIV-like ATRs, select-style success responses, and zero-length TLV objects, but the PKCS15/PIV object path either did not bind deeply enough or handled the supplied empty tags cleanly.
2. When `no_crash x apdu_stream_clean_or_feature_not_selected` appears for `opensc-fuzz-reader-chunks`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The fuzzer input is a sequence of little-endian length-prefixed chunks. The first chunk becomes the reader ATR. Later chunks are returned as APDU responses, with the final two response bytes interpreted as status words and the preceding bytes copied as response data.
- Harness: The harness installs a fake OpenSC reader, connects a card, binds PKCS15, and consumes APDU response chunks front-to-back. After binding, additional chunks supply operation inputs and parameters for object operations.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.

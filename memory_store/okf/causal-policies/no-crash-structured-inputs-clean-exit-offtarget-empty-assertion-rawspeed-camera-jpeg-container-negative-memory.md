---
type: causal-policy
title: "No Crash Structured Inputs Clean Exit Offtarget Empty Assertion Rawspeed Camera Jpeg Container Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal structured_inputs_clean_exit_offtarget_empty_assertion."
failure_class: "no_crash"
verifier_signal: "structured_inputs_clean_exit_offtarget_empty_assertion"
candidate_family: "construct"
input_format: "rawspeed-camera-file-or-jpeg-container"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "structured-inputs-clean-exit-offtarget-empty-assertion", "negative-memory", "round-10"]
match_keys: ["no_crash", "structured_inputs_clean_exit_offtarget_empty_assertion", "rawspeed-camera-file-or-jpeg-container", "afl-libfuzzer-wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Structured Inputs Clean Exit Offtarget Empty Assertion Rawspeed Camera Jpeg Container Negative Memory

## Policy
For `no_crash x structured_inputs_clean_exit_offtarget_empty_assertion`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. The empty input only triggered a harness assertion and also crashes the fixed build.
2. When `no_crash x structured_inputs_clean_exit_offtarget_empty_assertion` appears for `rawspeed-camera-file-or-jpeg-container`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The target bug is in lossless JPEG SOF parsing where component count must be consistent with row geometry before later row access. Reaching it likely requires a recognizable camera container that selects an LJPEG decoder and carries coherent image dimensions, strip data, and component metadata.
- Harness: The verifier runs a RawSpeed AFL-style parser/get-decoder/decode wrapper on raw file bytes. An empty file aborts in harness setup, while nonempty candidate containers are parsed or rejected without a target sanitizer report.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.

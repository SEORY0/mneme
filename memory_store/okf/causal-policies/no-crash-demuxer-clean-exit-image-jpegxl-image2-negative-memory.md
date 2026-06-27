---
type: causal-policy
title: "No Crash Demuxer Clean Exit Image Jpegxl Image2 Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal demuxer_clean_exit."
failure_class: "no_crash"
verifier_signal: "demuxer_clean_exit"
candidate_family: "seed_mutate"
input_format: "image/jpegxl-or-image2"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "demuxer-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "demuxer_clean_exit", "image/jpegxl-or-image2", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Demuxer Clean Exit Image Jpegxl Image2 Negative Memory

## Policy
For `no_crash x demuxer_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Valid JPEG XL, JPEG, PNG, BMP, and a filename-trailer variant all exited cleanly in the selected FFmpeg image2 demuxer target.
2. When `no_crash x demuxer_clean_exit` appears for `image/jpegxl-or-image2`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- JPEG XL samples begin as valid still or animated image codestream/container data. The selected image2 demuxer can also be influenced by the generic demux fuzzer metadata trailer that controls buffering, seekability, virtual filesize, and filename/extension hints.
- Harness: The FFmpeg demux fuzzer feeds raw bytes through a custom AVIO context. For non-flat builds it can reserve a trailer for IO controls and filename hints, but this run reported the image2 demux target rather than the expected animated JPEG XL demux target.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.

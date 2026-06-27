---
type: causal-policy
title: "No Crash Decompressor Clean Or Exception Rawspeed Ljpeg Decompressor Envelope Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal decompressor_clean_or_exception."
failure_class: "no_crash"
verifier_signal: "decompressor_clean_or_exception"
candidate_family: "construct"
input_format: "rawspeed-ljpeg-decompressor-envelope"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decompressor-clean-or-exception", "negative-memory", "round-10"]
match_keys: ["no_crash", "decompressor_clean_or_exception", "rawspeed-ljpeg-decompressor-envelope", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Decompressor Clean Or Exception Rawspeed Ljpeg Decompressor Envelope Negative Memory

## Policy
For `no_crash x decompressor_clean_or_exception`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A direct RawSpeed envelope with a minimal lossless-JPEG marker sequence did not reach a crashing slice write.
2. When `no_crash x decompressor_clean_or_exception` appears for `rawspeed-ljpeg-decompressor-envelope`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The direct decompressor envelope begins with little-endian scalar RawImage metadata, followed by tile offsets/flags and then a lossless JPEG byte stream. The JPEG stream must satisfy SOI, DHT, SOF3, and SOS gates before decoded samples are written into the RawImage buffer.
- Harness: The fuzzer consumes the whole input as a little-endian ByteStream. It creates RawImage metadata from the front fields, reads offset and compatibility fields, allocates image data, constructs LJpegDecompressor over the remaining bytes, and catches RawSpeed exceptions.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.

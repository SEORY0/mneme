---
type: causal-policy
title: "No Crash Compress Yuv Clean Bmp Source Image Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal compress_yuv_clean."
failure_class: "no_crash"
verifier_signal: "compress_yuv_clean"
candidate_family: "seed_mutate"
input_format: "bmp-source-image"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-memory"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "compress-yuv-clean", "bmp-source-image", "negative-memory", "round-12"]
match_keys: ["no_crash", "compress_yuv_clean", "bmp-source-image", "libfuzzer", "use-of-uninitialized-memory", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Compress Yuv Clean Bmp Source Image Negative Memory

- key: `no_crash x compress_yuv_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[bmp-source-image]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Compression seed images, truncation variants, and dimension-patched BMP carriers loaded or failed cleanly under the active compress_yuv fuzzer. No local sanitizer report appeared for the malloc-backed JPEG/YUV destination buffers.

## Policy
Treat `no_crash x compress_yuv_clean` on `bmp-source-image` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The active target loads an image file from the raw bytes, most practically BMP-like source images from the compression seed corpus. It iterates several pixel formats, subsampling modes, quality settings, and compression options, then encodes to YUV and compresses to JPEG.

## Harness Contract
The fuzzer writes raw bytes to a temporary image file, loads it with TurboJPEG image loading, allocates source-derived YUV and JPEG destination buffers with malloc, enables no-reallocation for compression, and touches compressed output bytes only when the API reports success.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `compress_yuv_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

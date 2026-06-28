---
type: causal-policy
title: "No Crash Decoder Returned Cleanly Bmp Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal decoder_returned_cleanly."
failure_class: "no_crash"
verifier_signal: "decoder_returned_cleanly"
candidate_family: "construct"
input_format: "bmp"
harness_convention: "file-reader"
vuln_class: "bounds-check-missing-header-size"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-returned-cleanly", "bmp", "negative_memory", "round-8"]
match_keys: ["no_crash", "decoder_returned_cleanly", "bmp", "file-reader", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Decoder Returned Cleanly Bmp Negative Memory

## Policy
Treat `no_crash x decoder_returned_cleanly` as a persistent failure basin for `bmp` under `file-reader`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Constructed BMP files exercised header/DIB boundary cases and palette boundary cases but did not trigger the loader assertion or out-of-bounds path. The vulnerable build may require a more precise interaction with ICO-embedded DIB handling or a later pixel-frame request.

## Format and Harness Gates
- Format: BMP files have a file header, a DIB header whose declared size selects the DIB variant, an optional color table for indexed formats, and pixel data starting at a declared data offset. Correct validation must account for both the file header and DIB size when checking bounds.
- Harness: The wrapper reads the whole file and invokes the Serenity image decoder on those raw bytes. The observable output reports only file length and process success unless a verifier-relevant crash occurs.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.

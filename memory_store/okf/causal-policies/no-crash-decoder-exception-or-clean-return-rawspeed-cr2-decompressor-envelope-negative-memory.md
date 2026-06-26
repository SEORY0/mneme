---
type: causal-policy
title: "No Crash Decoder Exception Or Clean Return Rawspeed Cr2 Decompressor Envelope Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal decoder_exception_or_clean_return."
failure_class: "no_crash"
verifier_signal: "decoder_exception_or_clean_return"
candidate_family: "construct"
input_format: "rawspeed-cr2-decompressor-envelope"
harness_convention: "libfuzzer"
vuln_class: "slice-width-miscalculation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-exception-or-clean-return", "rawspeed-cr2-decompressor-envelope", "negative_memory", "round-8"]
match_keys: ["no_crash", "decoder_exception_or_clean_return", "rawspeed-cr2-decompressor-envelope", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Decoder Exception Or Clean Return Rawspeed Cr2 Decompressor Envelope Negative Memory

## Policy
Treat `no_crash x decoder_exception_or_clean_return` as a persistent failure basin for `rawspeed-cr2-decompressor-envelope` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Envelope fields reached the Cr2Decompressor harness shape, and single-slice width variants were tried, but the synthetic compressed payload did not form a valid enough LJpeg frame to drive decodeN_X_Y into the slice-copy invariant.

## Format and Harness Gates
- Format: The fuzzer-specific RawSpeed envelope starts with little-endian raw image metadata, followed by little-endian slicing fields, then an LJpeg-compressed payload consumed by the decompressor. For the single-slice case, the last-slice width is the meaningful width for the only slice.
- Harness: The harness reads fields front-to-back from a ByteStream, creates a RawImage, reads slice count, regular slice width, and last-slice width, then constructs Cr2Decompressor and calls decode. Exceptions are swallowed; only memory safety failures count.

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

---
type: causal-policy
title: "No Crash Decoder Returned Cleanly Encoded Image Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal decoder_returned_cleanly."
failure_class: "no_crash"
verifier_signal: "decoder_returned_cleanly"
candidate_family: "seed_mutate"
input_format: "encoded-image"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-function-pointer"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-returned-cleanly", "encoded-image", "negative_memory", "round-8"]
match_keys: ["no_crash", "decoder_returned_cleanly", "encoded-image", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Decoder Returned Cleanly Encoded Image Negative Memory

## Policy
Treat `no_crash x decoder_returned_cleanly` as a persistent failure basin for `encoded-image` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Real PNG/JPEG image seeds and truncation mutations reached OpenCV imdecode but did not select the vulnerable function-pointer path. The target likely requires a specific codec or metadata feature rather than generic image parsing.

## Format and Harness Gates
- Format: The imdecode harness auto-detects image formats from raw encoded bytes. Ordinary PNG and JPEG samples are accepted; truncated PNG inputs are rejected by the image library without crashing.
- Harness: The harness passes the entire raw byte buffer to OpenCV imdecode. There is no fuzzer-side header, mode selector, or FuzzedDataProvider contract.

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

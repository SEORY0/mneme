---
type: causal-policy
title: "No Crash Valid Stream Decoded Without Target Crash Flac Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal valid_stream_decoded_without_target_crash."
failure_class: "no_crash"
verifier_signal: "valid_stream_decoded_without_target_crash"
candidate_family: "seed_mutate"
input_format: "flac"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "valid-stream-decoded-without-target-crash", "flac", "negative_memory", "round-8"]
match_keys: ["no_crash", "valid_stream_decoded_without_target_crash", "flac", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Valid Stream Decoded Without Target Crash Flac Negative Memory

## Policy
Treat `no_crash x valid_stream_decoded_without_target_crash` as a persistent failure basin for `flac` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Multiple valid metadata-heavy FLAC seeds and end truncations decoded without reaching the vulnerable bitreader boundary. The target likely requires a frame or subframe bitstream length inconsistency after the metadata gates, not just a valid container or one-byte EOF truncation.

## Format and Harness Gates
- Format: FLAC inputs begin with the native stream marker followed by metadata blocks and audio frames. Metadata seeds are useful parser-reaching envelopes, but the bitreader target appears tied to compressed frame contents and bit-level residual/subframe boundaries.
- Harness: The decoder fuzzer consumes raw FLAC file bytes. No front selector is used; a valid stream marker and coherent metadata are the primary reachability gates.

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

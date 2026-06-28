---
type: causal-policy
title: "No Crash Encoder Config Not Reached Or No Target Crash Xaac Encoder Fdp Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal encoder_config_not_reached_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "encoder_config_not_reached_or_no_target_crash"
candidate_family: "seed_mutate"
input_format: "xaac-encoder-fdp"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "encoder-config-not-reached-or-no-target-crash", "xaac-encoder-fdp", "negative_memory", "round-8"]
match_keys: ["no_crash", "encoder_config_not_reached_or_no_target_crash", "xaac-encoder-fdp", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Encoder Config Not Reached Or No Target Crash Xaac Encoder Fdp Negative Memory

## Policy
Treat `no_crash x encoder_config_not_reached_or_no_target_crash` as a persistent failure basin for `xaac-encoder-fdp` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- A decoder-style AAC seed did not match the selected encoder fuzzer contract. The missing gate is a front-loaded FuzzedDataProvider configuration that creates a valid encoder instance and leaves enough residual bytes for at least one encode process call on the frame-info path.

## Format and Harness Gates
- Format: The target is not a conventional AAC bitstream parser; it is an encoder configuration plus synthetic PCM/input data stream. Relevant fields include bitrate, channel count, sample rate, frame length, audio object type, SBR/eSBR/USAC and DRC-related switches, followed by remaining bytes used as encoder input.
- Harness: The libFuzzer target uses FuzzedDataProvider from the front of the input for encoder configuration fields, with some booleans selecting enum-like choices versus raw values. After initialization, the remaining bytes are consumed as input buffers or fill values for repeated encoder process calls.

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

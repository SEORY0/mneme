---
type: causal-policy
title: "Libavc Encoder Config Frame Construct Generic Crash Target Confirmed By Submit Verified Recovery"
description: "Round 10 verified recovery for generic_crash with verifier signal generic_crash_target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "generic_crash_target_confirmed_by_submit"
candidate_family: "construct"
input_format: "libavc-encoder-config-plus-frame-bytes"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-stack-struct-use"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "generic-crash-target-confirmed-by-submit", "libavc-encoder-config-plus-frame-bytes", "verified-recovery", "round-10"]
match_keys: ["generic_crash", "generic_crash_target_confirmed_by_submit", "libavc-encoder-config-plus-frame-bytes", "libfuzzer", "uninitialized-stack-struct-use", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# Libavc Encoder Config Frame Construct Generic Crash Target Confirmed By Submit Verified Recovery

## Policy
For `generic_crash x generic_crash_target_confirmed_by_submit`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Provide the raw encoder fuzzer configuration prefix with small valid dimensions, a supported color format, and encoder settings that allow initialization, followed by enough frame payload for at least one encode call.
2. A semi-planar color-format configuration reached the vulnerable encoder call and crashed the old build while the fixed build returned cleanly.

## Format Contract
- The encoder fuzzer consumes a fixed front-loaded configuration region for dimensions, color format, architecture, rate-control, quality, GOP, SEI, dynamic-change, and end-of-stream flags. Remaining bytes are expanded or split into YUV frame planes according to the selected color format.
- Harness: The libFuzzer input is raw bytes. Inputs shorter than the configuration prefix are ignored; successful candidates must satisfy encoder initialization before frame bytes are passed to the encode API.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

---
type: causal-policy
title: "Camera Seed Mutate Parser Reached Target Confirmed By Submit Verified Recovery"
description: "Round 10 verified recovery for wrong_sink with verifier signal parser_reached_target_confirmed_by_submit."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed_by_submit"
candidate_family: "seed_mutate"
input_format: "camera-raw"
harness_convention: "afl/libfuzzer-compatible-raw-file"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed-by-submit", "camera-raw", "verified-recovery", "round-10"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed_by_submit", "camera-raw", "afl/libfuzzer-compatible-raw-file", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# Camera Seed Mutate Parser Reached Target Confirmed By Submit Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_confirmed_by_submit`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a real RAW seed that passes LibRaw open and unpack, then let the processing loop exercise interpolation modes.
2. The valid camera RAW structure is what matters: it reaches LibRaw metadata parsing and post-unpack processing, where the vulnerable build exits nonzero and the fixed build exits cleanly.

## Format Contract
- LibRaw accepts complete camera RAW files such as TIFF-derived NEF/CR2 and RAF containers. The harness requires metadata and image payloads that pass open-buffer and unpack before postprocessing is attempted.
- Harness: The target reads a whole raw file buffer up to its size cap, calls open_buffer, calls unpack, then iterates through several processing quality modes. The built target reports AFL-style single-file execution but still runs the same fuzzer entry point.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

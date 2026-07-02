---
type: causal-policy
title: "BMP Construct Parser Reached Target Stack Heap Oob Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_stack_heap_oob_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_heap_oob_read"
candidate_family: "construct"
input_format: "bmp"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack-heap-oob-read", "bmp", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_stack_heap_oob_read", "bmp", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# BMP Construct Parser Reached Target Stack Heap Oob Read Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack_heap_oob_read`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a syntactically valid BMP header that advertises a normal uncompressed raw image with large dimensions, but provide only the header and no backing pixel rows.
2. The GPAC image reframer accepts the BMP metadata, computes output size and row stride from the declared dimensions, then copies rows from beyond the supplied input buffer.
3. A small dimension variant reached the parser without crashing; increasing only the declared image extent triggered the intended read.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- BMP detection relies on the bitmap magic and a valid file and DIB header.
- For uncompressed raw images, the bit depth controls bytes per pixel and each input row is padded to a word-aligned stride.
- Pixel data begins at the file-header data offset, while decoded output size is derived from declared width, height, and pixel format.
- Harness [[libfuzzer]]:
  - The GPAC fuzz target treats the raw input bytes as a media asset and lets probe/analyze select the image reframer from file content.
  - There is no front selector and no FuzzedDataProvider contract; satisfying the BMP header gates is enough to reach the BMP branch in the image reframing filter.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[bmp]] and [[libfuzzer]].

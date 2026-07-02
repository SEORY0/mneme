---
type: causal-policy
title: "Jpeg Exif Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "jpeg-exif"
harness_convention: "libfuzzer-libexif-loader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "jpeg-exif", "libfuzzer-libexif-loader", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "jpeg-exif", "libfuzzer-libexif-loader", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Jpeg Exif Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal valid JPEG APP1 EXIF carrier with a TIFF directory chain from the primary image directory to the EXIF directory.
2. Put a MakerNote entry in the EXIF directory whose value is copied into an exact-sized entry allocation and is a short, non-terminated prefix of the Apple maker-note signature.
3. This satisfies the EXIF parser and vendor-detection gates, then the Apple identifier treats the bounded MakerNote bytes as a C string and reads past the allocation.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- JPEG EXIF parsing accepts an APP1 EXIF segment containing an EXIF marker, a TIFF byte-order/header section, and IFD entries.
- IFD entries encode tag, format, component count, and either inline or pointed value data.
- The MakerNote tag is copied into an ExifEntry buffer sized from the format and component count before vendor-specific maker-note identification runs.
- Harness [[libfuzzer-libexif-loader]]:
  - The libFuzzer harness feeds raw input bytes directly to libexif loader/from-data paths.
  - There is no mode byte and no FuzzedDataProvider carving; the input itself must be a recognizable JPEG/EXIF or raw EXIF/TIFF payload.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[jpeg-exif]] and [[libfuzzer-libexif-loader]].

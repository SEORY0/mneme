---
type: causal-policy
title: "Bmp Construct Parser Reached Rle Streamer Overread Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_rle_streamer_overread."
failure_class: "generic_crash"
verifier_signal: "parser_reached_rle_streamer_overread"
candidate_family: "construct"
input_format: "bmp"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-rle-streamer-overread", "bmp", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_rle_streamer_overread", "bmp", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Bmp Construct Parser Reached Rle Streamer Overread Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_rle_streamer_overread`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a structurally valid BMP carrier that passes the file header and information-header gates, selects indexed RLE compression, and starts bitmap data immediately after the header. Keep dimensions small and positive so bitmap allocation succeeds, then provide an incomplete RLE control sequence that enters the metadata branch without enough real compressed bytes. The vulnerable decoder sizes the RLE input streamer from the whole file rather than the remaining payload, so it reads past the supplied buffer; the fixed build rejects the truncated RLE payload cleanly.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[bmp]]: BMP input begins with a file header containing the magic and bitmap-data start, followed by a DIB header whose size selects the header variant. Indexed BMPs may have a color table before bitmap data. RLE BMPs carry compression metadata in the DIB header and then a byte-coded stream of encoded runs, escape/meta commands, literal runs, optional padding, and an end marker.
- Harness [[libfuzzer]]: The libFuzzer harness passes the raw input buffer directly to the LibGfx BMP memory loader. There is no prefix, mode selector, argv path wrapper, checksum layer, or FuzzedDataProvider back/front carving; reachability depends on the BMP bytes themselves.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[bmp]] and [[libfuzzer]].

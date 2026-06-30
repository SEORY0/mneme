---
type: causal-policy
title: "C Blosc2 Frame Seed Mutate Parser Reached Frame Get Vlmetalayers Heap Buffer Overflow Read Integer Overflow To Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_frame_get_vlmetalayers_heap_buffer_overflow_read."
failure_class: "generic_crash"
verifier_signal: "parser_reached_frame_get_vlmetalayers_heap_buffer_overflow_read"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "afl++ libfuzzer-compatible whole-buffer frame decompressor"
vuln_class: "integer-overflow-to-heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-frame-get-vlmetalayers-heap-buffer-overflow-read", "c-blosc2-frame", "afl-libfuzzer-compatible-whole-buffer-frame-decompressor", "seed-mutate", "integer-overflow-to-heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_frame_get_vlmetalayers_heap_buffer_overflow_read", "c-blosc2-frame", "afl++ libfuzzer-compatible whole-buffer frame decompressor", "integer-overflow-to-heap-buffer-overflow-read", "verified_recovery", "seed-mutate", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# C Blosc2 Frame Seed Mutate Parser Reached Frame Get Vlmetalayers Heap Buffer Overflow Read Integer Overflow To Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_frame_get_vlmetalayers_heap_buffer_overflow_read`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid contiguous C-Blosc2 frame with an existing variable-length metalayer so the frame magic, declared frame size, chunk table, trailer marker, and trailer footer remain accepted. Preserve the trailer envelope and mutate only the variable-length metalayer content-length field to a large positive value that overflows the trailer-relative bounds calculation; the vulnerable parser accepts the relation and copies beyond the in-memory frame, while the fixed parser rejects the inconsistent length.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[c-blosc2-frame]]: A C-Blosc2 frame uses a msgpack-like header with frame magic, declared header size, declared frame size, byte counts, chunk sizing metadata, compressed chunk payloads, a compressed offset-table chunk, and a msgpack-like trailer. The trailer can contain variable-length metalayer metadata: an index maps a metalayer name to a trailer-relative content record, and the content record carries a binary marker plus a declared content length. The trailer footer stores the trailer extent and a fingerprint marker.
- Harness [[afl-libfuzzer-compatible-whole-buffer-frame-decompressor]]: The harness is an afl++ standalone wrapper around a libFuzzer-style decompress-frame target. It reads the whole PoC file into memory and passes those raw bytes directly to the frame decompressor; there is no selector byte, no FuzzedDataProvider carving, and no checksum recomputation requirement.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[c-blosc2-frame]] and [[afl-libfuzzer-compatible-whole-buffer-frame-decompressor]].

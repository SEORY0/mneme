---
type: causal-policy
title: "C Blosc2 Frame Seed Mutate Parser Reached Special Chunk Creation Invalid Typesize Arithmetic Exception Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_special_chunk_creation."
failure_class: "generic_crash"
verifier_signal: "parser_reached_special_chunk_creation"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "libfuzzer"
vuln_class: "invalid-typesize-arithmetic-exception"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-special-chunk-creation", "c-blosc2-frame", "libfuzzer", "seed-mutate", "invalid-typesize-arithmetic-exception", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_special_chunk_creation", "c-blosc2-frame", "libfuzzer", "invalid-typesize-arithmetic-exception", "verified_recovery", "seed-mutate", "other"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# C Blosc2 Frame Seed Mutate Parser Reached Special Chunk Creation Invalid Typesize Arithmetic Exception Verified Recovery

## Policy
For `generic_crash x parser_reached_special_chunk_creation`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid contiguous C-Blosc2 frame seed so the frame magic, declared size, chunk payloads, offset/index chunk, and trailer are accepted. Mutate only the frame-level type-size field to the minimal invalid value. The accepted frame then reaches the special-chunk reconstruction path, where the vulnerable build uses that unchecked type size in arithmetic while the fixed build rejects the malformed header relation.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[c-blosc2-frame]]: A contiguous C-Blosc2 frame has a msgpack-like header with magic, declared header length, declared total frame length, uncompressed and compressed byte counts, frame type, codec/filter metadata, frame-level type size, block size, chunk size, optional metalayers, compressed chunk payloads, a compressed offsets/index chunk, and a trailer. The frame-level type size is distinct from ordinary chunk header metadata and matters when a frame offset denotes a special synthesized chunk.
- Harness [[libfuzzer]]: The libFuzzer target passes the raw input buffer directly to the C-Blosc2 in-memory frame loader. If frame reconstruction succeeds and the declared uncompressed byte count is below the harness limit, it allocates an output buffer and iterates chunk decompression. There is no prefix selector and no FuzzedDataProvider front/back carving.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[c-blosc2-frame]] and [[libfuzzer]].

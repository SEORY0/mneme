---
type: causal-policy
title: "Blosc2 Frame Construct Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "blosc2-frame"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "blosc2-frame", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached", "blosc2-frame", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Blosc2 Frame Construct Parser Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal serialized Blosc2 in-memory frame that passes the frame-length, trailer, metalayer-index, and usermeta gates.
2. Keep the frame structurally recognizable with positive uncompressed and chunk sizes so the harness opens it and attempts lazy chunk decompression, then make the header-declared compressed-data span place the derived frame-index chunk start beyond the real frame body.
3. The vulnerable path reads the missing index chunk while resolving a chunk offset; the fixed build rejects this inconsistent index placement.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A Blosc2 serialized frame begins with a msgpack-like frame header containing magic, header size, total frame size, uncompressed size, compressed-data size, type size, chunk size, thread counts, filter pipeline, and a metalayer index.
- Data chunks are followed by a compressed chunk-offset index, and a trailer at the end carries usermeta length and trailer length.
- The number of chunks is derived from uncompressed size and chunk size; the frame-index location is derived from header size plus compressed-data size.
- Harness [[libfuzzer]]:
  - The libFuzzer harness feeds the entire raw input as an in-memory serialized frame to the frame opener.
  - If opening succeeds, it allocates an output buffer from the declared uncompressed size and lazily decompresses each data chunk except the final frame-index chunk.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[blosc2-frame]] and [[libfuzzer]].

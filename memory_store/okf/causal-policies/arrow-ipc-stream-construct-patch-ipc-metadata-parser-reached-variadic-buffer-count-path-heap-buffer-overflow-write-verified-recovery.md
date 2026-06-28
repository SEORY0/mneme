---
type: causal-policy
title: "Arrow IPC Stream Construct Patch IPC Metadata Parser Reached Variadic Buffer Count Path Heap Buffer Overflow Write Verified Recovery"
description: "Round 16 verified recovery for wrong_sink with verifier signal parser_reached_variadic_buffer_count_path."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_variadic_buffer_count_path"
candidate_family: "construct_patch_ipc_metadata"
input_format: "arrow-ipc-stream"
harness_convention: "libfuzzer-arrow-ipc-stream"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-variadic-buffer-count-path", "arrow-ipc-stream", "construct-patch-ipc-metadata", "verified-recovery", "round-16"]
match_keys: ["wrong_sink", "parser_reached_variadic_buffer_count_path", "arrow-ipc-stream", "libfuzzer-arrow-ipc-stream", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 16
---
# Arrow IPC Stream Construct Patch IPC Metadata Parser Reached Variadic Buffer Count Path Heap Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink x parser_reached_variadic_buffer_count_path`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
- Generate a valid Arrow IPC stream containing a binary-view-style field so record-batch metadata carries variadic buffer counts. Keep the schema, message framing, and body buffers coherent, then mutate the variadic buffer count to an invalid negative value. The vulnerable reader casts that value to an unsigned size and resizes or indexes buffer storage using the huge count before the fixed build rejects the invalid metadata.
- Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
- If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Arrow IPC streams are framed messages containing FlatBuffer schema and record-batch metadata followed by aligned buffers. Binary-view and string-view arrays use normal buffers plus a variadic-buffer-count vector that tells the reader how many additional character buffers belong to each array.
- Harness: The Arrow IPC stream fuzzer consumes the raw input bytes directly as an IPC stream and opens record batches through the standard stream reader. There is no leading mode byte, external schema file, or checksum gate.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-16 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

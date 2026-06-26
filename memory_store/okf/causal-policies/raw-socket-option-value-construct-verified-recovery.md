---
type: causal-policy
title: "Raw Socket Option Value Construct Verified Recovery"
description: "Round 6 verified recovery for wrong_sink with verifier signal target_like_heap_read."
failure_class: "wrong_sink"
verifier_signal: "target_like_heap_read"
candidate_family: "construct"
input_format: "raw socket option value"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-like-heap-read", "raw-socket-option-value", "construct", "verified-recovery", "round-6"]
match_keys: ["wrong_sink", "target_like_heap_read", "raw socket option value", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# Raw Socket Option Value Construct Verified Recovery

## Policy
For `wrong_sink x target_like_heap_read`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Provide a non-empty option buffer in the key-size class used by CURVE key options, but omit a string terminator within the supplied extent. The socket-options fuzzer eventually applies that same buffer to the CURVE option and the vulnerable setter treats it as a C string, reading past the fuzzer-provided allocation.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- There is no outer file format. The raw bytes are reused as the value for many ZeroMQ socket options. For CURVE public/secret/server keys, the meaningful structure is a fixed-size text key whose length and termination must be respected by the option parser.
- Harness: The harness creates sockets, iterates through the socket option range, calls setsockopt with the entire fuzzer byte buffer and its explicit size, and then tries getsockopt. It does not carve selector fields from the input; reachability depends on the loop hitting the vulnerable option with a buffer length in the sensitive range.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

---
type: causal-policy
title: "ZMTP V1 Construct Local Wrapper Not Exercised But Official Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 27 verified recovery for no_crash with verifier signal local_wrapper_not_exercised_but_official_target_match."
failure_class: "no_crash"
verifier_signal: "local_wrapper_not_exercised_but_official_target_match"
candidate_family: "construct"
input_format: "zmtp-v1"
harness_convention: "libfuzzer-mock-tcp"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-wrapper-not-exercised-but-official-target-match", "zmtp-v1", "libfuzzer-mock-tcp", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-27"]
match_keys: ["no_crash", "local_wrapper_not_exercised_but_official_target_match", "zmtp-v1", "libfuzzer-mock-tcp", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# ZMTP V1 Construct Local Wrapper Not Exercised But Official Target Match Heap Buffer Overflow Write Verified Recovery

## Policy
For `no_crash x local_wrapper_not_exercised_but_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a raw unversioned ZMTP v1 stream that first satisfies the routing-id frame expectation, then sends a large frame body so the v1 decoder's fixed static allocator metadata is resized as though it owned a larger buffer.
2. Follow with more frame data so the next read uses the enlarged size against the fixed allocation.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- ZMTP v1 is a raw frame stream rather than a file container.
- The unversioned path is selected before the modern greeting path; v1 frames are length-prefixed and carry a flags byte before the body.
- The initial routing-id/message frame must be accepted before later message-body frames exercise allocator behavior.
- Harness [[libfuzzer-mock-tcp]]:
  - The libFuzzer input is sent as raw bytes through a mock TCP peer to a ZeroMQ socket.
  - There is no leading mode byte, archive wrapper, checksum gate, or FuzzedDataProvider splitting; all supplied bytes become the peer's transport stream.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[zmtp-v1]] and [[libfuzzer-mock-tcp]].

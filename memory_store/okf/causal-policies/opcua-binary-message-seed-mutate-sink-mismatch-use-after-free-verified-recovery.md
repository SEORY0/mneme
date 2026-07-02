---
type: causal-policy
title: "Opcua Binary Message Seed Mutate Sink Mismatch Use After Free Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "seed_mutate"
input_format: "opcua-binary-message"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "opcua-binary-message", "libfuzzer", "seed-mutate", "use-after-free", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "sink_mismatch", "opcua-binary-message", "libfuzzer", "use-after-free", "verified_recovery", "seed-mutate", "use-after-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Opcua Binary Message Seed Mutate Sink Mismatch Use After Free Verified Recovery

## Policy
For `wrong_sink x sink_mismatch`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a valid OPC UA binary-message corpus sequence for channel setup, session creation and activation, subscription creation, publish queuing, deletion of the final subscription, and session close. Keep all chunk framing and session-token structure from the seed sequence, and mutate only the delete-subscriptions request so it targets the subscription created by this shortened sequence. This queues the no-subscription publish response callback, then queues session removal; shutdown drains removal first, leaving the delayed callback with a freed session pointer.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[opcua-binary-message]]: The input is a concatenation of complete OPC UA TCP binary chunks. Each chunk carries a message/chunk type, an internal chunk length, secure-channel metadata, request sequencing, and an encoded service NodeId followed by the service request body. Service requests after session creation depend on a valid authentication token; the fuzz build helps by copying the created token into subsequent request headers, so preserving seed chunk structure is more important than rebuilding the protocol from scratch.
- Harness [[libfuzzer]]: The libFuzzer entrypoint receives raw bytes, copies the full buffer into a UA_ByteString, and calls the binary message processor once. The connection layer walks all complete chunks in the buffer according to each chunk's embedded length. After message processing, the harness deletes the message, runs server shutdown, then deletes the server and connection; shutdown drains delayed callbacks in this single-threaded build.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[opcua-binary-message]] and [[libfuzzer]].

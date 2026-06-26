---
type: causal-policy
title: "Generic Crash Sink Mismatch Perfetto Trace Protobuf Negative Memory"
description: "Round 7 negative memory for generic_crash with verifier signal sink_mismatch."
failure_class: "generic_crash"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "perfetto-trace-protobuf"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "sink-mismatch", "perfetto-trace-protobuf", "negative-memory", "round-7"]
match_keys: ["generic_crash", "sink_mismatch", "perfetto-trace-protobuf", "libfuzzer", "stack-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# Generic Crash Sink Mismatch Perfetto Trace Protobuf Negative Memory

- key: `generic_crash x sink_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[perfetto-trace-protobuf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Direct TracePacket framing with memory snapshot nodes and root-like edge endpoints produced a local
process crash but did not reproduce the official vulnerable/fixed differential. Wrapped Trace
protobuf framing did not reach the memory snapshot parser.

## Policy
Treat `generic_crash x sink_mismatch` on `perfetto-trace-protobuf` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `sink_mismatch`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
Perfetto traces can carry TracePacket protobuf messages. A memory tracker snapshot packet contains
process snapshots, allocator dump nodes with ids and absolute names, and memory edges that reference
node ids with optional importance.

## Harness Contract
The trace processor fuzzer parses the raw input as Perfetto trace data and calls NotifyEndOfFile,
which flushes accumulated memory tracker snapshots. There is no separate mode byte.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.

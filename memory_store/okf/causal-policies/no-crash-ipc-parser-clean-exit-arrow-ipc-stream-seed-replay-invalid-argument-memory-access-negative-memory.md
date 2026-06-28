---
type: negative-memory
title: "No Crash Ipc Parser Clean Exit Arrow Ipc Stream Seed Replay Invalid Argument Memory Access Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal ipc_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "ipc_parser_clean_exit"
candidate_family: "seed_replay"
input_format: "arrow-ipc-stream"
harness_convention: "afl-file"
vuln_class: "invalid-argument-memory-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ipc-parser-clean-exit", "arrow-ipc-stream", "afl-file", "seed-replay", "negative-memory", "round-25"]
match_keys: ["no_crash", "ipc_parser_clean_exit", "arrow-ipc-stream", "afl-file", "invalid-argument-memory-access", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Ipc Parser Clean Exit Arrow Ipc Stream Seed Replay Invalid Argument Memory Access Negative Memory

- key: `no_crash x ipc_parser_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[arrow-ipc-stream]]
- related harness facts: [[afl-file]]

## Failure Shape
Existing in-repo Arrow IPC crash seeds were accepted by the active IPC stream fuzzer but did not trigger the described SliceBuffer or Slice family crash. The missing relation is likely a valid IPC schema/record-batch metadata pair whose buffer offset or logical slice bounds are accepted until slice construction, not a generic historical crash seed.

## Policy
Treat `no_crash x ipc_parser_clean_exit` on `arrow-ipc-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `ipc_parser_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ipc_parser_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Arrow IPC stream inputs use the Arrow streaming/file container with schema messages followed by record batch metadata and buffers. Parser reachability depends on preserving FlatBuffer metadata consistency with the message body and buffer layout.

## Harness Contract
The active target is an AFL-style file/stdin harness for arrow-ipc-stream-fuzz. It consumes the whole file as an IPC stream; there is no leading selector or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.

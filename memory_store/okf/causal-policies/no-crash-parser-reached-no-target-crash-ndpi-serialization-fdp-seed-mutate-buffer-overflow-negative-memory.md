---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Ndpi Serialization Fdp Seed Mutate Buffer Overflow Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "ndpi-serialization-fdp"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "ndpi-serialization-fdp", "libfuzzer", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "ndpi-serialization-fdp", "libfuzzer", "buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached No Target Crash Ndpi Serialization Fdp Seed Mutate Buffer Overflow Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ndpi-serialization-fdp]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Shipped serialization corpus seeds and an all-high scalar stress input exercised the serializer harness cleanly without violating the target buffer relation.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `ndpi-serialization-fdp` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_no_target_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The serialization harness is not a wire format; FuzzedDataProvider bytes select serializer format, initial buffer size, repeated scalar/string/binary values, block/list operations, snapshot and rollback behavior, buffer length mutation, and deserializer cloning.

## Harness Contract
The harness consumes control scalars through FuzzedDataProvider and then uses remaining bytes as short strings or binary payloads. Reaching the target likely requires aligning terminal scalar consumption with serializer buffer-length changes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 4 attempts.
- Scope: generator repair and basin avoidance only.

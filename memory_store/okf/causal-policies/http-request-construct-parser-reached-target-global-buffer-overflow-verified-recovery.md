---
type: causal-policy
title: "Http Request Construct Parser Reached Target Global Buffer Overflow Verified Recovery"
description: "Round 10 verified recovery for wrong_sink with verifier signal parser_reached_target_global_buffer_overflow."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_global_buffer_overflow"
candidate_family: "construct"
input_format: "http-request"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-global-buffer-overflow", "http-request", "verified-recovery", "round-10"]
match_keys: ["wrong_sink", "parser_reached_target_global_buffer_overflow", "http-request", "libfuzzer", "global-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# Http Request Construct Parser Reached Target Global Buffer Overflow Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_global_buffer_overflow`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a syntactically ordinary HTTP request with a valid request line and enough separate header fields to exceed the parser helper fixed header-start capacity.
2. The invariant violated is that the parser records header boundary pointers before enforcing the array capacity.

## Format Contract
- The request parser accepts a normal method, path, version line followed by repeated header lines and a blank line terminator. Each parsed header contributes boundary metadata, so header count is the controlling structure rather than body content.
- Harness: The fuzz harness feeds the raw file bytes directly to the Lwan HTTP request parser. There is no mode byte or provider-carved trailer; preserving a valid request-line and header-line grammar is enough to reach header parsing.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

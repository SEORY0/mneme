---
type: causal-policy
title: "Raw Date String Construct Parser Reached Null Dereference Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "raw-date-string"
harness_convention: "libfuzzer"
vuln_class: "null-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "raw-date-string", "libfuzzer", "construct", "null-dereference", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached", "raw-date-string", "libfuzzer", "null-dereference", "verified_recovery", "construct", "null-pointer-dereference"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Raw Date String Construct Parser Reached Null Dereference Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Feed the date parser a raw string that has no complete numeric date and contains invalid UTF-8. This reaches the month-name matching path after tokenization; the vulnerable build attempts Unicode normalization/case handling before validating the input and later dereferences a null normalized string in the month matcher. The fixed build rejects the invalid text before that path.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[raw-date-string]]: The input is not a container format: the harness copies raw bytes into a NUL-terminated string and passes that directly to the date parser. The parser first extracts integer-like tokens, and when it does not have a full numeric date it falls back to matching localized month names after UTF-8 casefolding and normalization. There are no magic, length, checksum, or record-table gates.
- Harness [[libfuzzer]]: The libFuzzer harness consumes the entire file as raw bytes. It does not use FuzzedDataProvider, does not carve a mode byte, and does not prepend metadata; the only transformation is making a temporary NUL-terminated copy before calling the date parsing API.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[raw-date-string]] and [[libfuzzer]].

---
type: causal-policy
title: Parser Executed Clean Negative Memory
description: Negative memory for candidates that reached a parser or device surface but did not violate the target invariant.
failure_class: no_crash
verifier_signal: parser_executed_no_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, parser_executed_no_crash, no_sanitizer_signal, negative_memory]
match_keys: [no_crash, parser_executed_no_crash, pdf_device_executed_no_crash, pdfwrite_executed_no_crash, dwarf_parser_executed_no_crash, arw_tiff_parser_executed_no_crash, decode_fuzzer_executed_no_crash]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Parser execution without a sanitizer signal means the carrier is useful but the vulnerable sub-invariant stayed satisfied. Preserve the carrier and change the inner semantic condition rather than restarting from random input.

## Procedure
1. Keep the accepted outer parser or device envelope.
2. Identify the sub-invariant still missing: malformed resource object, decoder-state transition, frame relationship, maker-note length, or table index.
3. Mutate the smallest inner field that affects that invariant.
4. Re-run verifier after each semantic mutation.
5. Quarantine broad mutations that keep producing clean parser execution.

## Negative Memory
- Do not discard a reached parser envelope.
- Do not submit clean parser executions.
- Do not confuse device or parser initialization with reaching the vulnerable inner operation.

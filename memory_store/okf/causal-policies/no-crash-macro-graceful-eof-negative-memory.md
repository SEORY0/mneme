---
type: causal-policy
title: Macro Graceful EOF Negative Memory
description: Negative memory for assembler macro candidates that reach macro buffering but take the normal end-of-file diagnostic path.
failure_class: no_crash
verifier_signal: macro_parser_reached_graceful_eof
candidate_family: construct
input_format: gas-assembly
harness_convention: fuzz-as
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, macro_parser_reached_graceful_eof, gas, macro, negative_memory]
match_keys: [no_crash, macro_parser_reached_graceful_eof, gas_macro_eof]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Assembler macro EOF diagnostics are negative memory for simple unterminated macro shapes. A successful candidate must avoid the normal EOF error while still leaving the internal line-buffer sentinel or repetition state inconsistent.

## Procedure
1. Keep syntax close enough to enter macro buffering.
2. Prefer nested macro, repetition, or directive terminator interactions over simple truncation.
3. Avoid forms that immediately report graceful EOF.
4. Change one terminator relationship at a time.
5. Verify that the output changes from graceful diagnostic to sanitizer signal before submitting.

## Negative Memory
- Do not repeat plain unterminated macro bodies.
- Do not grow filler lines when the diagnostic path is unchanged.
- Do not treat normal assembler errors as crash evidence.

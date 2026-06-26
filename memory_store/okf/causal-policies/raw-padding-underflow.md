---
type: causal-policy
title: Raw Padding Underflow
description: Verified recovery for wrong_sink with parser_reached_target_stack on raw padding buffer inputs.
failure_class: wrong_sink
verifier_signal: parser_reached_target_stack
candidate_family: construct
input_format: raw padding buffer
harness_convention: mode-padding fuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-target-stack, construct, raw-padding-buffer, verified_recovery]
match_keys: [wrong-sink, parser-reached-target-stack, raw-padding-buffer, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Raw Padding Underflow

- key: `wrong_sink x parser_reached_target_stack`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[raw-padding-buffer]]

## Failure Shape
A prior candidate family produced `wrong_sink` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `raw padding buffer` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Reach the reference padding checker with an input that contains only padding-equivalent bytes. The vulnerable loop uses an unsigned cursor while scanning backward, so the all-padding case underflows the cursor and reads before the buffer.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `wrong_sink` toward `parser_reached_target_stack`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

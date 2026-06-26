---
type: causal-policy
title: Zstd Legacy Raw Literal Overflow
description: Verified recovery for generic_crash with parser_reached_target_stack on zstd legacy frame inputs.
failure_class: generic_crash
verifier_signal: parser_reached_target_stack
candidate_family: construct
input_format: zstd legacy frame
harness_convention: libfuzzer simple_decompress
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-target-stack, construct, zstd-legacy-frame, verified_recovery]
match_keys: [generic-crash, parser-reached-target-stack, zstd-legacy-frame, stack-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Zstd Legacy Raw Literal Overflow

- key: `generic_crash x parser_reached_target_stack`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[zstd-legacy-frame]]

## Failure Shape
A prior candidate family produced `generic_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `zstd legacy frame` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Satisfy the harness seed prefix and the legacy frame-size scanner, including a terminal block marker. Use a compressed legacy block whose literal sub-block selects raw literals and declares a literal span larger than the fixed legacy literal buffer, so the raw literal copy overflows before sequence decoding matters.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `generic_crash` toward `parser_reached_target_stack`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

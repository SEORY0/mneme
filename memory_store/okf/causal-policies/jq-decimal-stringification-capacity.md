---
type: causal-policy
title: Jq Decimal Stringification Capacity
description: Verified recovery for generic_crash with target_numeric_stringification_overflow on jq-extended-json-fuzzer inputs.
failure_class: generic_crash
verifier_signal: target_numeric_stringification_overflow
candidate_family: construct
input_format: jq-extended-json-fuzzer
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, target-numeric-stringification-overflow, construct, jq-extended-json-fuzzer, verified_recovery]
match_keys: [generic-crash, target-numeric-stringification-overflow, jq-extended-json-fuzzer, heap-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Jq Decimal Stringification Capacity

- key: `generic_crash x target_numeric_stringification_overflow`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[jq-extended-json-fuzzer]]

## Failure Shape
A prior candidate family produced `generic_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `jq-extended-json-fuzzer` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use the extended jq parser envelope with parser and dump flags before the JSON text. Provide a valid decimal number whose exponent forces numeric stringification to need more output space than the allocated digit buffer, causing the decimal-to-string path to overflow during dumping.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `generic_crash` toward `target_numeric_stringification_overflow`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

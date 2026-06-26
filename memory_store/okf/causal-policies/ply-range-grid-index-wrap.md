---
type: causal-policy
title: Ply Range Grid Index Wrap
description: Verified recovery for generic_crash with parser_reached_sanitizer_crash on ply inputs.
failure_class: generic_crash
verifier_signal: parser_reached_sanitizer_crash
candidate_family: construct
input_format: ply
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-sanitizer-crash, construct, ply, verified_recovery]
match_keys: [generic-crash, parser-reached-sanitizer-crash, ply, out-of-bounds-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Ply Range Grid Index Wrap

- key: `generic_crash x parser_reached_sanitizer_crash`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[ply]]

## Failure Shape
A prior candidate family produced `generic_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `ply` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Build a valid ASCII PLY file with ordinary vertex data and a range-grid list that references an invalid vertex index. The vulnerable reader multiplies that reference by the point stride and checks the sum after arithmetic can wrap, then copies from an invalid position in the cloud data. The fixed reader rejects the invalid range-grid reference before copying.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `generic_crash` toward `parser_reached_sanitizer_crash`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

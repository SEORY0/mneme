---
type: causal-policy
title: Kbx Keyblock Length Wrap
description: Verified recovery for generic_crash with target_match on kbx inputs.
failure_class: generic_crash
verifier_signal: target_match
candidate_family: construct
input_format: kbx
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, target-match, construct, kbx, verified_recovery]
match_keys: [generic-crash, target-match, kbx, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Kbx Keyblock Length Wrap

- key: `generic_crash x target_match`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[kbx]]

## Failure Shape
A prior candidate family produced `generic_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `kbx` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Build a minimal keybox with a valid header blob followed by a syntactically valid PGP blob. Keep the keyblock offset inside the blob so the early range gate passes, but give the keyblock length a wrapped value so the offset-plus-length check underestimates the true span. The later PGP keyblock reader then over-reads the in-memory blob; the fixed build rejects the wrapped length relationship.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `generic_crash` toward `target_match`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

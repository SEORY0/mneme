---
type: causal-policy
title: Data Url Temporary Mime View Uaf
description: Verified recovery for generic_crash with server_vulnerable_crash_fix_clean on data-url inputs.
failure_class: generic_crash
verifier_signal: server_vulnerable_crash_fix_clean
candidate_family: construct
input_format: data-url
harness_convention: libfuzzer URL parser
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, server-vulnerable-crash-fix-clean, construct, data-url, verified_recovery]
match_keys: [generic-crash, server-vulnerable-crash-fix-clean, data-url, heap-use-after-free-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Data Url Temporary Mime View Uaf

- key: `generic_crash x server_vulnerable_crash_fix_clean`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[data-url]]

## Failure Shape
A prior candidate family produced `generic_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `data-url` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use a data URL whose MIME portion begins with a parameter separator rather than a type. The parser builds a default MIME prefix into a temporary string, then keeps a view into that temporary for URL construction, causing a dangling read in the vulnerable build.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `generic_crash` toward `server_vulnerable_crash_fix_clean`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

---
type: causal-policy
title: Json String Unescape Terminator
description: Verified recovery for generic_crash with target_match on json inputs.
failure_class: generic_crash
verifier_signal: target_match
candidate_family: construct
input_format: json
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, target-match, construct, json, verified_recovery]
match_keys: [generic-crash, target-match, json, heap-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Json String Unescape Terminator

- key: `generic_crash x target_match`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[json]]

## Failure Shape
A prior candidate family produced `generic_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `json` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use a valid JSON object with a string value, not a malformed escape. The media-type JSON dissector reaches the value callback, allocates an output buffer sized to the token, copies the value through the unescape routine, then writes the terminator just past the allocation. A moderately long printable value makes the one-byte heap write visible while remaining accepted by the parser.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `generic_crash` toward `target_match`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

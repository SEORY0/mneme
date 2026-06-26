---
type: causal-policy
title: Elf Section Group Member Bounds
description: Verified recovery for wrong_sink with section_group_oob_read on elf inputs.
failure_class: wrong_sink
verifier_signal: section_group_oob_read
candidate_family: construct
input_format: elf
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, section-group-oob-read, construct, elf, verified_recovery]
match_keys: [wrong-sink, section-group-oob-read, elf, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Elf Section Group Member Bounds

- key: `wrong_sink x section_group_oob_read`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[elf]]

## Failure Shape
A prior candidate family produced `wrong_sink` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `elf` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Build a minimal ELF with a valid section header table and a section-group payload. Keep the group syntactically valid, then make one group member reference the first section index outside the section table so the bounds check accepts it and the loader dereferences beyond the section array.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `wrong_sink` toward `section_group_oob_read`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

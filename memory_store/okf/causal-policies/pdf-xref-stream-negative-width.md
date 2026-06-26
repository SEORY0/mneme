---
type: causal-policy
title: Pdf Xref Stream Negative Width
description: Verified recovery for generic_crash with parser_reached_target_stack on pdf inputs.
failure_class: generic_crash
verifier_signal: parser_reached_target_stack
candidate_family: construct
input_format: pdf
harness_convention: libfuzzer ghostscript bmpmono device
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-target-stack, construct, pdf, verified_recovery]
match_keys: [generic-crash, parser-reached-target-stack, pdf, out-of-bounds-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Pdf Xref Stream Negative Width

- key: `generic_crash x parser_reached_target_stack`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[pdf]]

## Failure Shape
A prior candidate family produced `generic_crash` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `pdf` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Build a minimal PDF whose startxref points to an XRef stream object. Keep the stream dictionary valid enough to process, but include a negative width entry in the XRef stream field-width array so signed sizing and unsigned read length disagree during xref entry parsing.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `generic_crash` toward `parser_reached_target_stack`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.

---
type: causal-policy
title: "Elf Parser Reached Target Sink"
description: "Verified recovery for generic_crash with parser_reached_target_sink on elf inputs."
failure_class: generic_crash
verifier_signal: parser_reached_target_sink
candidate_family: construct
input_format: elf
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, parser-reached-target-sink, elf, heap-buffer-overflow-read, verified_recovery]
match_keys: [generic-crash, parser-reached-target-sink, elf, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Elf Parser Reached Target Sink

- key: `generic_crash x parser_reached_target_sink`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[elf]]

## Failure Shape
A candidate family ended at `generic_crash` before a verifier-confirmed repair. The successful shape kept the required `elf` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use a structurally valid ELF whose section table leads YARA into symbol parsing, with a symbol table linked to a string table that is accepted structurally but has no readable string bytes. The violated invariant is that a string-table pointer accepted by the format checks must still contain at least one byte before name lookup dereferences it.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_target_sink` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.

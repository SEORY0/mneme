---
type: causal-policy
title: "Elf Shared Object With Versioned Dynamic S Parser Reached Print Dynamic Symbol Stack "
description: "Verified recovery for wrong_sink with parser_reached_print_dynamic_symbol_stack_overflow on elf-shared-object-with-versioned-dynamic-symbol inputs."
failure_class: wrong_sink
verifier_signal: parser_reached_print_dynamic_symbol_stack_overflow
candidate_family: construct
input_format: elf-shared-object-with-versioned-dynamic-symbol
harness_convention: libfuzzer
vuln_class: stack-buffer-overflow-write
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, parser-reached-print-dynamic-symbol-stack-overflow, elf-shared-object-with-versioned-dynamic-symbol, stack-buffer-overflow-write, verified_recovery]
match_keys: [wrong-sink, parser-reached-print-dynamic-symbol-stack-overflow, elf-shared-object-with-versioned-dynamic-symbol, stack-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Elf Shared Object With Versioned Dynamic S Parser Reached Print Dynamic Symbol Stack

- key: `wrong_sink x parser_reached_print_dynamic_symbol_stack_overflow`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[elf-shared-object-with-versioned-dynamic-symbol]]

## Failure Shape
A candidate family ended at `wrong_sink` before a verifier-confirmed repair. The successful shape kept the required `elf-shared-object-with-versioned-dynamic-symbol` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Build a valid dynamically linked ELF shared object whose dynamic symbol table includes a symbol version string longer than the fixed stack scratch buffer used while computing printed symbol-name width. Keep the ELF headers, dynamic string table, dynamic symbol table, and version-definition records valid so readelf reaches dynamic symbol printing; only the version-name length violates the invariant.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `parser_reached_print_dynamic_symbol_stack_overflow` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.

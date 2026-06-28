---
type: causal-policy
title: "ELF Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 13 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "elf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "elf", "construct", "verified-recovery", "round-13"]
match_keys: ["generic_crash", "parser_reached_target_sink", "elf", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# ELF Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_sink`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a structurally valid ELF whose section table leads YARA into symbol parsing, with a symbol table linked to a string table that is accepted structurally but has no readable string bytes. The violated invariant is that a string-table pointer accepted by the format checks must still contain at least one byte before name lookup dereferences it.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- YARA's ELF module consumes raw ELF bytes, validates the outer ELF and section-header structure, then resolves symbol names through the linked string table for symbol-table entries. A symbol table and its linked string table must be internally coherent enough for the module to reach symbol-name resolution.

## Harness Contract
- The libFuzzer target compiles a YARA rule importing the ELF module and scans the input buffer directly. There is no selector byte, file wrapper, argv layer, or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
## Round 13 Reinforcement

- key: `generic_crash x parser_reached_target_sink`
- candidate family: `construct`
- related format facts: [[elf]]
- related harness facts: [[libfuzzer]]

### Procedure Delta
Use a structurally valid ELF whose section table leads YARA into symbol parsing, with a symbol table linked to a string table that is accepted structurally but has no readable string bytes. The violated invariant is that a string-table pointer accepted by the format checks must still contain at least one byte before name lookup dereferences it.

### Format Contract Delta
YARA's ELF module consumes raw ELF bytes, validates the outer ELF and section-header structure, then resolves symbol names through the linked string table for symbol-table entries. A symbol table and its linked string table must be internally coherent enough for the module to reach symbol-name resolution.

### Harness Contract Delta
The libFuzzer target compiles a YARA rule importing the ELF module and scans the input buffer directly. There is no selector byte, file wrapper, argv layer, or FuzzedDataProvider carving.

### Evidence Shape
- Support: additional round-13 official target match.
- Scope: generator repair for the same failure-keyed basin.

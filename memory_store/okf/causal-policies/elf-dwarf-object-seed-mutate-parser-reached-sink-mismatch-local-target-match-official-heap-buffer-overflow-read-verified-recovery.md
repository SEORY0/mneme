---
type: causal-policy
title: "Elf Dwarf Object Seed Mutate Parser Reached Sink Mismatch Local Target Match Official Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_local_target_match_official."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_local_target_match_official"
candidate_family: "seed_mutate"
input_format: "elf-dwarf-object"
harness_convention: "afl-libfuzzer-compatible"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-local-target-match-official", "elf-dwarf-object", "afl-libfuzzer-compatible", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_local_target_match_official", "elf-dwarf-object", "afl-libfuzzer-compatible", "heap-buffer-overflow-read", "verified_recovery", "seed-mutate", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Elf Dwarf Object Seed Mutate Parser Reached Sink Mismatch Local Target Match Official Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_local_target_match_official`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a real ELF debug object so object detection, abbreviation parsing, and DIE traversal succeed. Add a DWARF type-unit view because this harness iterates type units, add a minimal macro section plus a CU macro attribute so macro-context construction calls source-file lookup, and keep the CU statement-list reference pointing at the line table. Replace the line table with a structurally valid experimental two-level header that passes the legacy-list, marker, directory, and file-table gates but ends exactly before the experimental subprogram table's format-count field. The vulnerable build accepts equality with section end and reads one byte past the line section; the fixed build rejects the boundary.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[elf-dwarf-object]]: The input must be a complete ELF/DWARF object, not a raw DWARF section. The relevant object needs section headers naming debug types, abbreviations, line data, and macro data. A DWARF4 type unit has the common unit header plus a type signature and type-offset field before the first DIE. The experimental two-level line table has the usual line-table prefix, a standard-opcode operand table, empty legacy directory and file lists, an experimental marker, logical and actual table offsets, DWARF5-style directory and file tables, and then an experimental subprogram table.
- Harness [[afl-libfuzzer-compatible]]: The harness writes the raw bytes to a temporary file, initializes libdwarf from the file descriptor, requests the next type-unit header, obtains the root DIE, and calls the DWARF5 macro-context API. Macro-context setup loads the macro section, reads the CU macro attribute, and calls source-file lookup, which loads and parses the line table. No FuzzedDataProvider carving is used.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[elf-dwarf-object]] and [[afl-libfuzzer-compatible]].

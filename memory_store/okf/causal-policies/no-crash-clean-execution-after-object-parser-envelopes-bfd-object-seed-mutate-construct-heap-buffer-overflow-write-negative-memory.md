---
type: negative-memory
title: "No Crash Clean Execution After Object Parser Envelopes Bfd Object Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal clean_execution_after_object_parser_envelopes."
failure_class: "no_crash"
verifier_signal: "clean_execution_after_object_parser_envelopes"
candidate_family: "seed_mutate+construct"
input_format: "bfd-object"
harness_convention: "libfuzzer-raw-file"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-execution-after-object-parser-envelopes", "bfd-object", "libfuzzer-raw-file", "seed-mutate-construct", "heap-buffer-overflow-write", "negative-memory", "round-28"]
match_keys: ["no_crash", "clean_execution_after_object_parser_envelopes", "bfd-object", "libfuzzer-raw-file", "heap-buffer-overflow-write", "negative_memory", "construct", "seed-mutate", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Clean Execution After Object Parser Envelopes Bfd Object Negative Memory

- key: `no_crash x clean_execution_after_object_parser_envelopes`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[bfd-object]]
- harnesses: [[libfuzzer-raw-file]]

## Dead-End Shape
The raw objdump harness accepted real and constructed object envelopes, but the candidates did not create a live BFD section where the logical allocation size stayed smaller than the size used by full-section reads. Plain ELF section headers expose one logical size, oversized or unreadable sections were rejected or skipped cleanly, a COFF auxiliary-symbol relation stayed on a clean parser path, and a compressed debug section was not enough to force the raw/logical section-size split in the active dump mode.

## Policy
For `no_crash x clean_execution_after_object_parser_envelopes` on `bfd-object`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `seed_mutate+construct` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[bfd-object]]: BFD object inputs are auto-detected binary object files. ELF objects use a section-header string table plus section headers naming debug, string, symbol, and payload sections; section flags distinguish contents, allocation, debug, and compressed sections. COFF objects use a fixed file header, section headers with raw-data pointers, and an optional symbol table whose records can declare auxiliary entries. The vulnerable helper reads full section contents using BFD section metadata, and some callers preallocate a debug-section buffer from the logical section size before asking BFD to fill it.
- Harness [[libfuzzer-raw-file]]: The libFuzzer wrapper writes the raw input bytes unchanged to a temporary file and drives the objdump display path with section contents, headers, private headers, debug sections, stabs, and disassembly enabled. There is no FuzzedDataProvider layout, checksum, mode selector, or extra envelope. BFD determines the object flavor from the raw file, and the objdump configuration avoids global decompression when raw section-content dumping is enabled.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.

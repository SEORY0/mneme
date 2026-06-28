---
type: causal-policy
title: "PE Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal parser_reached_target_stack."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "pe"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-stack", "pe", "construct", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "parser_reached_target_stack", "pe", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# PE Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_stack`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a minimal PE image with a valid DOS stub, PE header, optional header, one section, and a debug data-directory entry. Make the debug directory itself fit and mark its entry as CodeView, but point the CodeView raw-data RVA to a mapped location at the file tail that is too short for the CodeView signature read. Keep the section mapping valid so RVA-to-file-offset conversion succeeds before the target read.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A PE image needs a DOS magic and e_lfanew pointer to a PE signature, a COFF file header, an optional header with data directories, and at least one section whose virtual address and raw file offset let YARA translate RVAs. The debug data directory stores an RVA and size; each debug entry contains a type plus an RVA for the raw CodeView data.
- Harness: The libFuzzer harness scans the raw input bytes with a compiled YARA rule importing the PE module. There is no file wrapper, selector byte, or FuzzedDataProvider carving; the PE module is loaded while evaluating the rule and walks the memory block directly.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

---
type: causal-policy
title: "ELF With Stabs Debug Sections Construct Parser Reached Stabs Nearest Line Underflow Segmentation Fault Stabs String Table Underflow Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal parser_reached_stabs_nearest_line_underflow."
failure_class: "generic_crash"
verifier_signal: "parser_reached_stabs_nearest_line_underflow"
candidate_family: "construct"
input_format: "elf-with-stabs-debug-sections"
harness_convention: "libfuzzer-binutils-addr2line"
vuln_class: "segmentation-fault-stabs-string-table-underflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-stabs-nearest-line-underflow", "elf-with-stabs-debug-sections", "libfuzzer-binutils-addr2line", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "parser_reached_stabs_nearest_line_underflow", "elf-with-stabs-debug-sections", "libfuzzer-binutils-addr2line", "segmentation-fault-stabs-string-table-underflow", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# ELF With Stabs Debug Sections Construct Parser Reached Stabs Nearest Line Underflow Segmentation Fault Stabs String Table Underflow Verified Recovery

- key: `generic_crash x parser_reached_stabs_nearest_line_underflow`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[elf-with-stabs-debug-sections]]
- harnesses: [[libfuzzer-binutils-addr2line]]

## Failure Shape
Build a minimal ELF relocatable object that BFD accepts, with coherent section-name and symbol-string tables, allocated code sections that cover the addr2line harness's built-in address tokens, and present stabs debug sections. Keep the stabs record section loadable while making the paired stabs string table empty; once addr2line maps a requested address into an allocated section, nearest-line lookup enters the stabs backend and underflows the empty string table.

## Policy
For `generic_crash x parser_reached_stabs_nearest_line_underflow` on `elf-with-stabs-debug-sections`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `elf-with-stabs-debug-sections` carrier and `libfuzzer-binutils-addr2line` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `elf-with-stabs-debug-sections` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
ELF object reachability depends on a coherent ELF header, section header table, section-name string table, and BFD-recognized allocated sections. Stabs debug data uses a record section plus a companion string table; BFD finds these sections by their conventional names, loads their contents, and then builds a nearest-line index from fixed-size stabs records. An empty stabs string table is structurally representable but violates the backend assumption that the loaded string table has a last byte to terminate.

## Harness Contract
The libFuzzer addr2line harness writes the raw input bytes to a temporary file and invokes the addr2line processing path on that file. It supplies built-in address-like strings rather than reading stdin; strings beginning with hexadecimal letters are parsed as numeric addresses, not symbol names, so the ELF must contain allocated sections covering those parsed addresses before nearest-line lookup is reached. There is no prefix selector or FuzzedDataProvider split.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 5 attempts.
- Scope: generator repair and retargeting only.

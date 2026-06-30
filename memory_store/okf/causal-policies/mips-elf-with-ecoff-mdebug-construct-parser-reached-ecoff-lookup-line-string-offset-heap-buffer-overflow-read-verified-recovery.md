---
type: causal-policy
title: "Mips Elf With Ecoff Mdebug Construct Parser Reached Ecoff Lookup Line String Offset Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_ecoff_lookup_line_string_offset."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_ecoff_lookup_line_string_offset"
candidate_family: "construct"
input_format: "mips-elf-with-ecoff-mdebug"
harness_convention: "honggfuzz-libfuzzer-binutils-addr2line-wrapper"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-ecoff-lookup-line-string-offset", "mips-elf-with-ecoff-mdebug", "honggfuzz-libfuzzer-binutils-addr2line-wrapper", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_ecoff_lookup_line_string_offset", "mips-elf-with-ecoff-mdebug", "honggfuzz-libfuzzer-binutils-addr2line-wrapper", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Mips Elf With Ecoff Mdebug Construct Parser Reached Ecoff Lookup Line String Offset Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_ecoff_lookup_line_string_offset`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a small MIPS ELF object that BFD accepts and that contains an allocated code section covering the addr2line harness's built-in address queries. Add a coherent ECOFF-style .mdebug section with a symbolic header, file descriptor table, procedure descriptor table, local symbol table, local string table, and line table so nearest-line lookup reaches ecofflink lookup_line. Keep the PDR table allocation large enough to avoid the generic one-past PDR loop crash, then violate only the FDR filename string-offset invariant by pointing it just outside the local string table. The vulnerable build resolves the line and later reads past the local string table while printing the filename; the fixed build rejects or suppresses that invalid string reference.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[mips-elf-with-ecoff-mdebug]]: A usable carrier can be a MIPS ELF object with a .mdebug section whose ECOFF symbolic header stores absolute file offsets to debug sub-tables. The nearest-line path needs at least one allocated section covering the harness-supplied addresses, an FDR with procedure descriptors, a PDR table, a small line table, and a local string table. FDR filename and symbol name fields are string-table indexes; keeping table counts and offsets mutually consistent is necessary before mutating one string index.
- Harness [[honggfuzz-libfuzzer-binutils-addr2line-wrapper]]: The addr2line fuzz wrapper writes the raw input bytes to a temporary file, opens it through BFD, uses built-in address-like query strings, and maps over allocated sections before calling bfd_find_nearest_line_discriminator. There is no fuzzer prefix, FuzzedDataProvider split, checksum, archive wrapper, or stdin-provided address list.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[mips-elf-with-ecoff-mdebug]] and [[honggfuzz-libfuzzer-binutils-addr2line-wrapper]].

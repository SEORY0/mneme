---
type: causal-policy
title: "Mips ELF With Ecoff Mdebug Construct Parser Reached Target Filename Print Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_filename_print_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_filename_print_read"
candidate_family: "construct"
input_format: "mips-elf-with-ecoff-mdebug"
harness_convention: "libfuzzer-binutils-addr2line"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-filename-print-read", "mips-elf-with-ecoff-mdebug", "libfuzzer-binutils-addr2line", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_filename_print_read", "mips-elf-with-ecoff-mdebug", "libfuzzer-binutils-addr2line", "heap-buffer-overflow-read", "wrong-sink", "parser-reached-target-filename-print-read", "mips-elf-with-ecoff-mdebug", "libfuzzer-binutils-addr2line", "heap-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Mips ELF With Ecoff Mdebug Construct Parser Reached Target Filename Print Read Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_filename_print_read`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[mips-elf-with-ecoff-mdebug]]
- related harness facts: [[libfuzzer-binutils-addr2line]]

## Policy
For `wrong_sink x parser_reached_target_filename_print_read` on `mips-elf-with-ecoff-mdebug`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a compact MIPS ELF object with an allocated text range that covers the addr2line harness query addresses and a coherent ECOFF .mdebug section. The symbolic header must point to valid line, procedure, file-descriptor, and local-string tables using absolute file positions. Keep the logical procedure range valid while allocating enough procedure records to avoid the known lookup-loop overread, then make the FDR filename reference a valid local-string entry whose table is not NUL-terminated. The vulnerable build returns that filename and the output path reads past the allocated string; the fixed build avoids the overread.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[mips-elf-with-ecoff-mdebug]]: MIPS ELF .mdebug uses a MIPS-specific section type and an ECOFF symbolic header. The header stores absolute file positions and counts for line bytes, PDR records, FDR records, local strings, and optional symbol tables. ECOFF-32 external FDR records contain compact 16-bit procedure index/count fields, while PDR records carry full procedure VMAs used by nearest-line lookup. FDR filename fields are offsets into the local string table and can be selected without requiring local symbols when only a filename is needed.
- Harness [[libfuzzer-binutils-addr2line]]: libFuzzer writes the raw input bytes to a temporary file and invokes the addr2line processing path after a precondition check. The harness supplies fixed command-line address strings; addr2line parses these as hexadecimal PCs, maps them over allocated sections, and calls BFD nearest-line lookup with a section-relative offset. There is no FuzzedDataProvider or prefix mode byte.

## Negative Memory
- Do not corrupt the outer `mips-elf-with-ecoff-mdebug` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[mips-elf-with-ecoff-mdebug]] and [[libfuzzer-binutils-addr2line]].

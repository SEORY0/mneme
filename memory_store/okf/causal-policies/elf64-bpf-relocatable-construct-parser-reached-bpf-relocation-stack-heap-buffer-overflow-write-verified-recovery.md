---
type: causal-policy
title: "Elf64 Bpf Relocatable Construct Parser Reached Bpf Relocation Stack Heap Buffer Overflow Write Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_bpf_relocation_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_bpf_relocation_stack"
candidate_family: "construct"
input_format: "elf64-bpf-relocatable"
harness_convention: "libfuzzer-addr2line-file"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-bpf-relocation-stack", "elf64-bpf-relocatable", "libfuzzer-addr2line-file", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_bpf_relocation_stack", "elf64-bpf-relocatable", "libfuzzer-addr2line-file", "heap-buffer-overflow-write", "wrong-sink", "parser-reached-bpf-relocation-stack", "elf64-bpf-relocatable", "libfuzzer-addr2line-file", "heap-buffer-overflow-write", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Elf64 Bpf Relocatable Construct Parser Reached Bpf Relocation Stack Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_bpf_relocation_stack`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[elf64-bpf-relocatable]]
- related harness facts: [[libfuzzer-addr2line-file]]

## Policy
For `wrong_sink x parser_reached_bpf_relocation_stack` on `elf64-bpf-relocatable`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a coherent little-endian BPF ELF relocatable object with a symbol table, section-name table, an allocated code section that makes addr2line enter line lookup, and a DWARF info section with a relocation section. Use a defined local section symbol so debug relocation is performed rather than cleared. The triggering relocation is a non-64 BPF instruction relocation whose generic size check accepts the field, while the relocation installer writes at the instruction bit-position beyond the checked field inside the small debug section.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[elf64-bpf-relocatable]]: BPF ELF64 relocatable inputs need mutually consistent ELF header fields, section headers, section-name strings, symbol table, string table, and RELA section metadata. A RELA section links to the symbol table and names its target section via section-header info. BPF instruction relocation types carry a bit-position that refers to an instruction subfield rather than the beginning of the checked relocation field.
- Harness [[libfuzzer-addr2line-file]]: The addr2line libFuzzer harness writes the raw input bytes to a temporary file, checks that BFD recognizes an object, canonicalizes symbols if present, then calls addr2line processing with fixed address strings. Addr2line maps over allocated sections; when an address falls in one, BFD line lookup loads DWARF info and uses relocated debug-section contents when symbols are available.

## Negative Memory
- Do not corrupt the outer `elf64-bpf-relocatable` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[elf64-bpf-relocatable]] and [[libfuzzer-addr2line-file]].

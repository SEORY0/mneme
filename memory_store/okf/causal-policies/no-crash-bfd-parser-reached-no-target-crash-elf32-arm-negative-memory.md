---
type: causal-policy
title: "No Crash Bfd Parser Reached No Target Crash Elf32 Arm Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal bfd_parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "bfd_parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "elf32-arm"
harness_convention: "libfuzzer"
vuln_class: "elf-plt-synthetic-symbol-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "bfd-parser-reached-no-target-crash", "elf32-arm", "negative-memory", "round-12"]
match_keys: ["no_crash", "bfd_parser_reached_no_target_crash", "elf32-arm", "libfuzzer", "elf-plt-synthetic-symbol-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Bfd Parser Reached No Target Crash Elf32 Arm Negative Memory

- key: `no_crash x bfd_parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf32-arm]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed little-endian ARM ELF files were recognized by BFD and printed by the objdump-style fuzzer, including variants with empty or undersized PLT sections and larger PLT relocation tables. They did not reach a crashing synthetic symbol table allocation/copy pattern.

## Policy
Treat `no_crash x bfd_parser_reached_no_target_crash` on `elf32-arm` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The carrier is an ELF32 little-endian ARM object or executable. BFD recognition requires a valid ELF header and section table. The target invariant involves the relationship between the PLT section size, ARM PLT entry sizing, and the number of PLT relocations used when synthetic symbols are generated.

## Harness Contract
The fuzzer writes raw input bytes to a temporary file and runs a binutils/BFD display path that performs target detection, section dumping, disassembly, and synthetic symbol processing when the object format and options allow it.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `bfd_parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

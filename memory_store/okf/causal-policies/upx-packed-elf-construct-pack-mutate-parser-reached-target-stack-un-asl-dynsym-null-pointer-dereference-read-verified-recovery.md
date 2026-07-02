---
type: causal-policy
title: "Upx Packed Elf Construct Pack Mutate Parser Reached Target Stack Un Asl Dynsym Null Pointer Dereference Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_target_stack_un_asl_dynsym."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_stack_un_asl_dynsym"
candidate_family: "construct_pack_mutate"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-upx-test-file"
vuln_class: "null-pointer-dereference-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-stack-un-asl-dynsym", "upx-packed-elf", "libfuzzer-upx-test-file", "construct-pack-mutate", "null-pointer-dereference-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_target_stack_un_asl_dynsym", "upx-packed-elf", "libfuzzer-upx-test-file", "null-pointer-dereference-read", "verified_recovery", "construct", "null-pointer-dereference"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Upx Packed Elf Construct Pack Mutate Parser Reached Target Stack Un Asl Dynsym Null Pointer Dereference Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_stack_un_asl_dynsym`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a small shared-object ELF that has a dynamic symbol table, a dynamic string table, an initializer, and an exported absolute symbol whose name is one of the ASLR adjustment names recognized by UPX. Pack it as an Android-style shared library so UPX forwards the section headers and treats it as a packed shared object. Then mark the packed file as old-style ASLR shared-library input, keep the forwarded header cut point consistent with the decompressed ELF header span, and remove the dynamic string-table advertisement without removing the dynamic symbol table. During test-mode unpacking, the ASLR dynsym adjustment sees the absolute symbol, tries to resolve its name through a missing dynstr pointer, and crashes in the vulnerable build while the fixed build skips that processing.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[upx-packed-elf]]: A useful UPX-packed ELF carrier for this bug is a packed Linux shared object, not a plain executable. The carrier needs normal ELF headers, load segments, a PT_DYNAMIC table, a SHT_DYNSYM section, a dynamic string table, an initializer entry, and the UPX pack metadata/trailer so test mode recognizes it as packed. Android-style shared-library packing forwards section headers into the packed file; an old-style ASLR marker plus a forwarded section-header cut point controls whether the unpacker enters the ASLR shared-library dynsym adjustment path. Absolute dynamic symbols named like common end-of-image symbols are specially adjusted in that path.
- Harness [[libfuzzer-upx-test-file]]: The libFuzzer harness writes the input bytes verbatim to a temporary file and invokes UPX test mode on that path. There is no mode byte, FuzzedDataProvider split, checksum wrapper, or length prefix outside the file itself; the bytes must be a complete UPX-packed file that passes packed-file recognition before unpack-time ELF logic is reached.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[upx-packed-elf]] and [[libfuzzer-upx-test-file]].

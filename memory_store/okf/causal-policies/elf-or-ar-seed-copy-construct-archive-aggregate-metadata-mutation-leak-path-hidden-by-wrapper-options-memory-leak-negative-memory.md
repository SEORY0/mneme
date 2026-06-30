---
type: negative-memory
title: "ELF Or Ar Seed Copy Construct Archive Aggregate Metadata Mutation Leak Path Hidden By Wrapper Options Memory Leak Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal leak_path_hidden_by_wrapper_options."
failure_class: "no_crash"
verifier_signal: "leak_path_hidden_by_wrapper_options"
candidate_family: "seed_copy|construct|archive_aggregate|metadata_mutation"
input_format: "elf-or-ar"
harness_convention: "libfuzzer objcopy"
vuln_class: "memory-leak"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "leak-path-hidden-by-wrapper-options", "elf-or-ar", "libfuzzer-objcopy", "seed-copy-construct-archive-aggregate-metadata-mutation", "memory-leak", "negative-memory", "round-29"]
match_keys: ["no_crash", "leak_path_hidden_by_wrapper_options", "elf-or-ar", "libfuzzer objcopy", "memory-leak", "no-crash", "leak-path-hidden-by-wrapper-options", "elf-or-ar", "libfuzzer-objcopy", "memory-leak", "negative_memory", "seed_copy|construct|archive_aggregate|metadata_mutation", "seed-copy-construct-archive-aggregate-metadata-mutation"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# ELF Or Ar Seed Copy Construct Archive Aggregate Metadata Mutation Leak Path Hidden By Wrapper Options Memory Leak Negative Memory

- key: `no_crash x leak_path_hidden_by_wrapper_options`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-or-ar]]
- related harness facts: [[libfuzzer-objcopy]]

## Failure Shape
The objcopy leak is reachable when the fuzz target is run directly with leak detection enabled, and the leak report points at the symbol-hash-table setup path. Under the actual benchmark wrapper, both the environment and the libFuzzer options suppress leak checking, so valid ELF inputs, debug-bearing ELF inputs, archive aggregation, and malformed symbol-table metadata all exit cleanly. The fixed build was not reached for the best candidates because the vulnerable build exit stayed zero.

## Policy
Treat `no_crash x leak_path_hidden_by_wrapper_options` on `elf-or-ar` for `memory-leak` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `leak_path_hidden_by_wrapper_options` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `leak_path_hidden_by_wrapper_options`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The harness accepts raw object-file bytes. Recognized inputs include ELF relocatable objects, ELF shared/executable objects, and ar archives containing object members. ELF symbol handling depends on the section-header table, the SYMTAB section metadata, its linked string table, and relocation sections that reference the symbol table. Archives use the standard ar global header followed by member headers and member object payloads.

## Harness Contract
The /bin/arvo wrapper runs the objcopy libFuzzer target on a copied PoC file path. The target writes the raw PoC bytes to a temporary file, initializes BFD once, creates objcopy symbol hash tables, and invokes copy_main with only an input path and output path. The PoC does not control argv flags, there is no FuzzedDataProvider carving, and the wrapper/options path disables libFuzzer leak detection.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 10 attempts.
- Scope: generator repair and basin avoidance only.

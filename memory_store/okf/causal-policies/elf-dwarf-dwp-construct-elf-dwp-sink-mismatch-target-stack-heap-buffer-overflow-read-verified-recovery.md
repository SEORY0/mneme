---
type: causal-policy
title: "Elf Dwarf Dwp Construct Elf Dwp Sink Mismatch Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal sink_mismatch_target_stack."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_target_stack"
candidate_family: "construct_elf_dwp"
input_format: "elf-dwarf-dwp"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-target-stack", "elf-dwarf-dwp", "libfuzzer", "construct-elf-dwp", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "sink_mismatch_target_stack", "elf-dwarf-dwp", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Elf Dwarf Dwp Construct Elf Dwp Sink Mismatch Target Stack Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x sink_mismatch_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a small ELF object containing DWO-style DWARF type-unit sections plus a package index for type units. Make the package index select an abbreviation contribution and make the type-unit header use a nonzero abbreviation-table displacement inside that contribution. Keep the type-unit contribution large enough to pass libdwarf's conservative header-size gate, then make the selected abbreviation entry end with an incomplete attribute/form pair at the contribution boundary. The vulnerable code bounds the abbreviation scan from the displaced pointer rather than from the contribution base, so the LEB decoder reads past the allocated abbreviation section while creating the CU context.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[elf-dwarf-dwp]]: The input is an ELF object whose relevant payload is split-DWARF package data. DWP package indexes contain a header, hash/index tables, a row of DW_SECT column identifiers, and per-unit offset and size rows for contributions such as type-unit data and abbreviation data. DWO type-unit sections carry a DWARF unit header with version, unit type, address size, abbreviation-table displacement, signature data, and a type-offset field before DIE bytes. The abbreviation section is a sequence of LEB128 abbreviation records: code, tag, child flag, then attribute/form pairs terminated by a zero pair.
- Harness [[libfuzzer]]: The libFuzzer target writes the raw input bytes to a temporary object file, initializes libdwarf with group-any section selection, calls the DWARF CU-header API with the type-section flag, then requests the root DIE and its child. There is no fuzzer-specific prefix or length carving; all structure is supplied by the ELF and DWARF sections themselves.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[elf-dwarf-dwp]] and [[libfuzzer]].

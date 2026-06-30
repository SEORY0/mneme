---
type: negative-memory
title: "X86 64 COFF Object Seed Mutate And Construct Non Target Crash Or Both Image Crash COFF Optional Header Output Corruption Negative Memory"
description: "Round 29 negative memory for generic_crash with verifier signal non_target_crash_or_both_image_crash."
failure_class: "generic_crash"
verifier_signal: "non_target_crash_or_both_image_crash"
candidate_family: "seed_mutate_and_construct"
input_format: "x86_64-coff-object"
harness_convention: "libfuzzer-binutils-objcopy"
vuln_class: "coff-optional-header-output-corruption"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "non-target-crash-or-both-image-crash", "x86-64-coff-object", "libfuzzer-binutils-objcopy", "seed-mutate-and-construct", "coff-optional-header-output-corruption", "negative-memory", "round-29"]
match_keys: ["generic_crash", "non_target_crash_or_both_image_crash", "x86_64-coff-object", "libfuzzer-binutils-objcopy", "coff-optional-header-output-corruption", "generic-crash", "non-target-crash-or-both-image-crash", "x86-64-coff-object", "libfuzzer-binutils-objcopy", "coff-optional-header-output-corruption", "negative_memory", "seed_mutate_and_construct", "seed-mutate-and-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# X86 64 COFF Object Seed Mutate And Construct Non Target Crash Or Both Image Crash COFF Optional Header Output Corruption Negative Memory

- key: `generic_crash x non_target_crash_or_both_image_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[x86-64-coff-object]]
- related harness facts: [[libfuzzer-binutils-objcopy]]

## Failure Shape
Valid x86_64 COFF seeds and constructed minimal objects could reach objcopy/BFD and sometimes the executable optional-header writer, but official comparison did not isolate the described vulnerable-only output-corruption path. Full seed mutation with debug metadata was too broad and crashed both builds; narrower executable objects were clean or nondeterministic rather than official target matches.

## Policy
Treat `generic_crash x non_target_crash_or_both_image_crash` on `x86_64-coff-object` for `coff-optional-header-output-corruption` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `non_target_crash_or_both_image_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `non_target_crash_or_both_image_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
A COFF object has a fixed file header with machine type, section count, optional-header length, symbol-table pointer/count, and flags. It is followed by an optional header when present, a table of section headers, raw section data, relocation/line metadata if any, then fixed-size symbol records and an optional string table. For the x86_64 COFF backend, marking an object executable is the important gate that makes objcopy synthesize an output optional header.

## Harness Contract
The objcopy fuzzer writes the raw libFuzzer bytes to a temporary file and invokes a fixed objcopy copy path with compression, extraction, and debug-related options. There is no selector byte or FuzzedDataProvider layout; BFD auto-detects the raw file as an object/archive format before objcopy writes a temporary output file.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 9 attempts.
- Scope: generator repair and basin avoidance only.

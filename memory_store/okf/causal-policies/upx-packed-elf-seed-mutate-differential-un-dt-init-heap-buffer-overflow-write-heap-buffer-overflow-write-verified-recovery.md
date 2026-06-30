---
type: causal-policy
title: "Upx Packed Elf Seed Mutate Differential Un Dt Init Heap Buffer Overflow Write Heap Buffer Overflow Write Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal differential_un_DT_INIT_heap_buffer_overflow_write."
failure_class: "wrong_sink"
verifier_signal: "differential_un_DT_INIT_heap_buffer_overflow_write"
candidate_family: "seed_mutate"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-file-command-wrapper"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "differential-un-dt-init-heap-buffer-overflow-write", "upx-packed-elf", "libfuzzer-file-command-wrapper", "seed-mutate", "heap-buffer-overflow-write", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "differential_un_DT_INIT_heap_buffer_overflow_write", "upx-packed-elf", "libfuzzer-file-command-wrapper", "heap-buffer-overflow-write", "verified_recovery", "seed-mutate", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Upx Packed Elf Seed Mutate Differential Un Dt Init Heap Buffer Overflow Write Heap Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink x differential_un_DT_INIT_heap_buffer_overflow_write`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a genuine UPX-packed Linux shared-object carrier that reaches the shared-library decompression path and the hard initializer-array restore path in un_DT_INIT. Preserve valid compressed payloads, payload checksums, and trailer metadata for the real trailer method. Then make a per-block method selector inconsistent with the trailer method while leaving that block's compressed bytes valid for the trailer method, and shape the dynamic restore pointer so it maps inside a LOAD segment but not to a complete relocation record inside the file image. The vulnerable build keeps using the stale trailer method, reaches un_DT_INIT, and writes restored relocation fields past the file image. The fixed build honors the per-block method selector and rejects before the restore write.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[upx-packed-elf]]: A useful UPX-packed Linux ELF input is a complete packed shared object with normal ELF and program headers, l_info and p_info records, b_info records carrying per-block uncompressed size, compressed size, method, and filter metadata, compressed payloads, a terminator record, and the final PackHeader plus overlay pointer. Packed shared-object carriers can preserve a PT_DYNAMIC table in the packed file. Initializer-array dynamic entries can drive the hard un_DT_INIT restore path; that path may use a dynamic null entry as a pointer to saved relocation storage and dynsym[0]-sized storage as replacement relocation fields. Dynamic values are virtual addresses that UPX maps through PT_LOAD headers before treating them as file-image pointers.
- Harness [[libfuzzer-file-command-wrapper]]: The libFuzzer harness writes the raw input bytes verbatim to a temporary file and invokes the UPX decompression command with an output-file argument. There is no mode byte, length prefix, checksum wrapper, or FuzzedDataProvider carving outside the file itself; reachability depends on UPX recognizing a complete packed executable and entering normal unpacking. The harness catches ordinary C++ exceptions, so sanitizer aborts are the useful crash signal.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[upx-packed-elf]] and [[libfuzzer-file-command-wrapper]].

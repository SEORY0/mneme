---
type: negative-memory
title: "Ghostscript Document With Embedded Truetype Construct And Seed Mutate Ghostscript Document Processed Without Truetype Interpreter Crash Heap Buffer Overflow Read Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal ghostscript_document_processed_without_truetype_interpreter_crash."
failure_class: "no_crash"
verifier_signal: "ghostscript_document_processed_without_truetype_interpreter_crash"
candidate_family: "construct-and-seed-mutate"
input_format: "ghostscript-document-with-embedded-truetype"
harness_convention: "libfuzzer-ghostscript-ps2write-device"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "ghostscript-document-processed-without-truetype-interpreter-crash", "ghostscript-document-with-embedded-truetype", "libfuzzer-ghostscript-ps2write-device", "construct-and-seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-29"]
match_keys: ["no_crash", "ghostscript_document_processed_without_truetype_interpreter_crash", "ghostscript-document-with-embedded-truetype", "libfuzzer-ghostscript-ps2write-device", "heap-buffer-overflow-read", "no-crash", "ghostscript-document-processed-without-truetype-interpreter-crash", "ghostscript-document-with-embedded-truetype", "libfuzzer-ghostscript-ps2write-device", "heap-buffer-overflow-read", "negative_memory", "construct-and-seed-mutate", "construct-and-seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# Ghostscript Document With Embedded Truetype Construct And Seed Mutate Ghostscript Document Processed Without Truetype Interpreter Crash Heap Buffer Overflow Read Negative Memory

- key: `no_crash x ghostscript_document_processed_without_truetype_interpreter_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ghostscript-document-with-embedded-truetype]]
- related harness facts: [[libfuzzer-ghostscript-ps2write-device]]

## Failure Shape
The attempted carriers preserved Ghostscript document parsing but did not produce a sanitizer-visible crash at the TrueType PUSHB interpreter. Attempts included a Type42 PostScript font with a mutated rendered glyph program, a Type42 font with mutated font-level bytecode tables, an embedded TrueType PDF font, a direct Type42 execution-operator call, a bare mutated TTF negative control, and unmodified Ghostscript document examples. The likely missing gate is a malformed sfnt or Type42 segmentation state where the interpreter code-size check passes while the operand reads cross the backing-buffer boundary; ordinary table mutation and normal embedding are handled cleanly or rejected.

## Policy
Treat `no_crash x ghostscript_document_processed_without_truetype_interpreter_crash` on `ghostscript-document-with-embedded-truetype` for `heap-buffer-overflow-read` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `ghostscript_document_processed_without_truetype_interpreter_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ghostscript_document_processed_without_truetype_interpreter_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Ghostscript TrueType execution is reached through a document-level carrier, usually PostScript Type42 or PDF TrueType FontFile2 embedding. Type42 fonts carry an sfnts array of hex strings, an Encoding mapping, and CharStrings mapping glyph names to TrueType glyph indices. Simple glyph instruction streams are followed by glyph outline bytes in the same glyph allocation, so a truncated PUSHB inside a simple glyph may not become a memory OOB even if it violates the logical bytecode length.

## Harness Contract
The wrapper runs the libFuzzer Ghostscript ps2write device target on the raw file contents as standard input. There is no mode byte, checksum, archive wrapper, or FuzzedDataProvider layout. The fuzzer invokes Ghostscript with ps2write output, quiet/batch/no-pause options, stdout redirected to stderr, and the document read from stdin.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 7 attempts.
- Scope: generator repair and basin avoidance only.

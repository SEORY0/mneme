---
type: causal-policy
title: "Bmp Construct Parser Reached Target Palette Reader Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_target_palette_reader."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_palette_reader"
candidate_family: "construct"
input_format: "bmp"
harness_convention: "libfuzzer-mupdf-document-renderer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 2
confidence: high
tags: ["wrong-sink", "parser-reached-target-palette-reader", "bmp", "libfuzzer-mupdf-document-renderer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_target_palette_reader", "bmp", "libfuzzer-mupdf-document-renderer", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Bmp Construct Parser Reached Target Palette Reader Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_palette_reader`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a raw BMP that MuPDF recognizes through image content sniffing. Keep the file header and DIB header valid, choose a palette-bearing indexed bit depth, and declare a bitmap-data position implying a full palette while providing too little palette data. The vulnerable loader computes the palette span from the declared bitmap position before clamping it to the actual buffer, so palette reads run past the supplied bytes; the fixed build rejects or clamps that relation.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[bmp]]: A BMP begins with a file header containing the signature and bitmap-data position, followed by a DIB header that declares dimensions, planes, bit depth, compression, optional palette color count, and image data size. Indexed BMP depths use palette entries between the DIB header and bitmap data; the entry size depends on the DIB family. The palette span is derived from the declared bitmap-data position and the palette-bearing bit depth.
- Harness [[libfuzzer-mupdf-document-renderer]]: The MuPDF libFuzzer target passes the raw bytes to fz_open_document_with_stream with PDF magic, but document handling first performs content sniffing on seekable streams. A BMP signature is enough for the image document handler to load the raw BMP as a page, and rendering that page calls the BMP subimage loader. There is no fuzzer prefix selector and no FuzzedDataProvider byte split.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[bmp]] and [[libfuzzer-mupdf-document-renderer]].

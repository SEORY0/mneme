---
type: causal-policy
title: "Pdf Construct Parser Reached Target Area Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_target_area_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_area_official_target_match"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-area-official-target-match", "pdf", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_target_area_official_target_match", "pdf", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Pdf Construct Parser Reached Target Area Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_area_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a syntactically valid one-page PDF with a normal catalog, pages tree, page object, resources dictionary, and matching xref/trailer. Set the page box to small positive dimensions below the render-time rounding threshold so PDFium accepts the page, libvips initializes an image with zero dimensions, and thumbnail generation reaches the invalid rectangle path that the fixed build rejects earlier.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[pdf]]: PDF reachability required a complete object graph rather than a header stub: catalog, pages node, page object, content stream, xref table, trailer, and startxref. PDFium accepted sub-unit page-box dimensions; at the default scale libvips rounded those dimensions to zero before downstream thumbnail processing.
- Harness [[libfuzzer]]: The libvips thumbnail fuzzer feeds the raw input bytes directly to vips_image_new_from_buffer with no leading mode byte or FuzzedDataProvider split. If loading succeeds, it rejects only very large dimensions or too many bands, then calls vips_thumbnail_image and computes an average over the output.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[pdf]] and [[libfuzzer]].

---
type: causal-policy
title: "Pdf With Embedded Type1C Cff Font Construct Parser Reached Stack Buffer Overflow Write Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "pdf-with-embedded-type1c-cff-font"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "pdf-with-embedded-type1c-cff-font", "libfuzzer", "construct", "stack-buffer-overflow-write", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached", "pdf-with-embedded-type1c-cff-font", "libfuzzer", "stack-buffer-overflow-write", "verified_recovery", "construct", "stack-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Pdf With Embedded Type1C Cff Font Construct Parser Reached Stack Buffer Overflow Write Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal, well-formed PDF with a page content stream that selects a font resource. The font descriptor must embed a CFF font program in a Type1C font stream so the pdfwrite target loads it through the PDF CFF reader. Keep the CFF header and INDEX structures valid, then put a compact real operand in a dictionary whose nibbles expand to the parser buffer's full printable capacity before a normal dictionary operator. The vulnerable reader appends the terminator past the fixed stack buffer; the fixed build bounds the expansion correctly.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[pdf-with-embedded-type1c-cff-font]]: A PDF carrier needs the normal catalog, pages, page, resources, font, font descriptor, embedded font stream, content stream, xref, and trailer gates. The embedded font stream is classified as CFF by its stream subtype and CFF header. CFF uses a header followed by Name, Top DICT, String, and Global Subr INDEX structures. Dictionary real operands are encoded as packed nibbles; numeric nibbles expand to one ASCII character, while exponent-minus style nibbles expand to two characters, and a terminator nibble ends the operand.
- Harness [[libfuzzer]]: The selected arvo wrapper runs the Ghostscript pdfwrite libFuzzer target and provides the file bytes as the single raw input consumed from stdin. There is no FuzzedDataProvider layout, mode selector, or prefix carving for this target. Earlier XPS and direct PostScript CFF attempts did not reach the selected pdfwrite CFF sink; the successful path is a raw PDF that causes the page interpreter to load the embedded Type1C font.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[pdf-with-embedded-type1c-cff-font]] and [[libfuzzer]].

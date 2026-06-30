---
type: causal-policy
title: "PDF With Embedded Type1 Font Construct Parser Reached PDF Type1 Key Compare Global Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_pdf_type1_key_compare."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_pdf_type1_key_compare"
candidate_family: "construct"
input_format: "pdf-with-embedded-type1-font"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-pdf-type1-key-compare", "pdf-with-embedded-type1-font", "libfuzzer", "construct", "global-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_pdf_type1_key_compare", "pdf-with-embedded-type1-font", "libfuzzer", "global-buffer-overflow-read", "wrong-sink", "parser-reached-pdf-type1-key-compare", "pdf-with-embedded-type1-font", "libfuzzer", "global-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# PDF With Embedded Type1 Font Construct Parser Reached PDF Type1 Key Compare Global Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_pdf_type1_key_compare`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[pdf-with-embedded-type1-font]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_pdf_type1_key_compare` on `pdf-with-embedded-type1-font`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal PDF page that forces loading of an embedded Type 1 font through the PDF font resource path. The embedded font stream only needs enough PostScript-like tokens to reach the Type 1 key-definition interpreter. Put a built-in encoding operator token in the key position of a definition so the vulnerable key checker compares that short static token against later longer Type 1 key names without first checking the token length.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[pdf-with-embedded-type1-font]]: A minimal PDF carrier needs a catalog, pages tree, page, font resource, font descriptor, embedded FontFile stream, and a content stream that selects the font. The Type 1 FontFile stream is interpreted as PostScript-like tokens with slash names, arrays, strings, and operators such as def. The crash can occur during early embedded-font key scanning before a complete glyph program is needed.
- Harness [[libfuzzer]]: libFuzzer supplies raw bytes as Ghostscript stdin through the gstoraster-style harness. There is no FuzzedDataProvider prefix or mode byte. Ghostscript sniffs the raw input as PDF/PostScript and renders to the cups device with output discarded.

## Negative Memory
- Do not corrupt the outer `pdf-with-embedded-type1-font` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[pdf-with-embedded-type1-font]] and [[libfuzzer]].

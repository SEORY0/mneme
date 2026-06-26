---
type: causal-policy
title: "PDF Seed Mutate Parser Reached Heap Use After Free Read Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "pdf", "seed-mutate", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "parser_reached", "pdf", "libfuzzer", "heap-use-after-free-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# PDF Seed Mutate Parser Reached Heap Use After Free Read Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a renderable PDF page with a content stream that enters text mode, selects a valid page font, and executes a TJ array. The array must survive parsing as an operand while a later text-showing error path causes the operand-stack reference to be removed; the vulnerable implementation then continues through TJ array access with only the stale local pointer. Rich font/resources and recovered stream structure can be enough to keep rendering active while the lifetime invariant is violated.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- PDF reachability for Ghostscript requires a recognizable PDF header, catalog, pages tree, page object with media box, page resources including fonts, and a content stream. Ghostscript can recover from some non-canonical object ordering and stream/xref inconsistencies, but the page must still be renderable. Text operations are postfix content-stream operators inside BT/ET; TJ consumes an array whose elements are strings or numeric glyph displacements.
- Harness: The libFuzzer harness feeds the input as raw stdin to Ghostscript configured for the CUPS raster device. There is no fuzzer-byte carving or FuzzedDataProvider layout; Ghostscript auto-detects PDF/PostScript and processes pages through the normal interpreter.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

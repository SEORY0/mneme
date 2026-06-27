---
type: causal-policy
title: "PDF Construct Parser Reached Target Area Verified Recovery"
description: "Round 10 verified recovery for wrong_sink with verifier signal parser_reached_target_area."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_area"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "raw PDF text extraction/render harness"
vuln_class: "container-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-area", "pdf", "verified-recovery", "round-10"]
match_keys: ["wrong_sink", "parser_reached_target_area", "pdf", "raw PDF text extraction/render harness", "container-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# PDF Construct Parser Reached Target Area Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_area`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a minimal renderable PDF with a valid page tree, font resource, and text-showing content so the page text-list/font-info code builds per-glyph metadata.
2. The violated invariant is assigning by index into a glyph cache vector that only reserved capacity and was never sized.

## Format Contract
- The PDF needs a header, catalog, pages node, page object, resources dictionary with a usable font, and a content stream whose declared length matches parseable text operators. A simple text object is sufficient to drive glyph metadata creation.
- Harness: The harness feeds raw bytes as a PDF and invokes Poppler page processing that reaches text extraction/font cache code. There is no input carving or checksum gate beyond normal PDF parseability.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

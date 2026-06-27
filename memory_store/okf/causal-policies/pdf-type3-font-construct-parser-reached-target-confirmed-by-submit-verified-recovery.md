---
type: causal-policy
title: "PDF Type3 Font Construct Parser Reached Target Confirmed By Submit Verified Recovery"
description: "Round 10 verified recovery for generic_crash with verifier signal parser_reached_target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_confirmed_by_submit"
candidate_family: "construct"
input_format: "pdf-type3-font"
harness_convention: "stdin-ghostscript-raster"
vuln_class: "graphics-state-reference-count-corruption"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-confirmed-by-submit", "pdf-type3-font", "verified-recovery", "round-10"]
match_keys: ["generic_crash", "parser_reached_target_confirmed_by_submit", "pdf-type3-font", "stdin-ghostscript-raster", "graphics-state-reference-count-corruption", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# PDF Type3 Font Construct Parser Reached Target Confirmed By Submit Verified Recovery

## Policy
For `generic_crash x parser_reached_target_confirmed_by_submit`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a small renderable PDF with a Type3 font used by page content.
2. The CharProc changes the stroking color before declaring glyph metrics with the bounding-box metrics operator, then draws simple content.
3. Rendering the glyph forces Ghostscript through CharProc graphics-state handling and triggers the vulnerable reference-count path; the fixed build survives.

## Format Contract
- A Type3 PDF font needs a font dictionary with font matrix, font bounding box, encoding differences, widths, CharProcs, and a page content stream that selects the font and shows the encoded glyph. CharProc streams can contain graphics operators and must declare glyph metrics before normal painting operations.
- Harness: The harness feeds the raw file through Ghostscript stdin using the CUPS raster device. The input must be a complete PDF that Ghostscript will render; standalone content streams are not enough.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

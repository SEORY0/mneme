---
type: causal-policy
title: "No Crash Parser Not Reached Opentype Font Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "opentype-font", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "opentype-font", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Opentype Font Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Valid bundled fonts and simple sfnt/table-directory mutations all stayed clean. The attempts likely reached general font parsing but did not construct the subset map state where glyph IDs outnumber corresponding offset values.
- When `no_crash x parser_not_reached` appears for `opentype-font`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input is a complete sfnt/OpenType font. The file begins with an sfnt version/tag and table directory, followed by table records and table payloads. HarfBuzz subset behavior depends on internally consistent table records and glyph/offset maps, so isolated byte flips in the header or ordinary shaping test fonts are not sufficient.
- Harness: The HarfBuzz subset fuzzer consumes raw font bytes as a whole font. There is no datasource envelope. Parser reach requires a valid enough sfnt/OpenType structure for the subset pipeline to load faces and build subset maps.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

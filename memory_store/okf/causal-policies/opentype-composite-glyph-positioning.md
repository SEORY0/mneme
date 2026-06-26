---
type: causal-policy
title: OpenType Composite Glyph Positioning Recovery
description: Recover font shaping crashes by preserving a valid OpenType seed and selecting composite glyph positioning.
failure_class: generic_crash
verifier_signal: sanitizer_or_process_crash
candidate_family: seed-sweep
input_format: opentype-font
harness_convention: libfuzzer
vuln_class: glyph-positioning-memory-safety
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, sanitizer_or_process_crash, opentype, composite_glyph, shaping]
match_keys: [generic_crash, sanitizer_or_process_crash, opentype-font, composite_glyph_positioning]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For shaping bugs in OpenType fonts, a valid seed that reaches variable or composite glyph processing is more valuable than a synthetic font. The causal path is composite glyph positioning, especially anchored component positioning applied outside its intended point class.

## Procedure
1. Start from a structurally valid OpenType font seed.
2. Prefer seeds that exercise HarfBuzz shaping, variable glyph data, or composite glyphs.
3. Preserve table directory validity and glyph reachability.
4. Mutate component positioning metadata rather than top-level font headers.
5. Submit only stable crashes that occur after shaping reaches the composite glyph path.

## Negative Memory
- Do not corrupt the sfnt table directory for shaping bugs.
- Do not keep broad seed sweeps that never exercise composite glyphs.
- Do not minimize away the glyph or shaping feature that selects the path.

---
type: format-family
title: OpenType font format
description: Format contract for shaping paths involving composite or variable glyph data.
resource: cybergym://format/opentype-font
tags: [opentype, font, shaping, composite_glyph]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
OpenType fonts require a valid sfnt table directory and enough glyph, layout, or variation data for a shaper to select the relevant glyph path.

## Invariants
- Table-directory validity is a reachability gate.
- Shaping bugs often need a real seed rather than a synthetic minimal font.
- Composite glyph positioning should be mutated without destroying glyph selection.

## Round 8 Factual Contract

### Schema / Invariants
- The input is an OpenType/TrueType-style font blob. The relevant path is HarfBuzz subsetting of variation data: the font must contain variation-store structures that survive parsing, enter subsetting, and then fail serialization at the specific point where later fields are still inspected.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 9 Factual Contract

### Schema / Invariants
- The target accepts raw OpenType/TrueType font bytes.
- Valid fonts need a normal sfnt table directory and shaping-relevant tables such as cmap/glyf or
  CFF plus metrics/layout tables; corrupting table offsets or lengths too broadly tends to be
  sanitized away before shaping.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

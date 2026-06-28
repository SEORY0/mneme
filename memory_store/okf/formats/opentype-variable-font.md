---
type: format-family
title: opentype-variable-font format
description: Structure, build skeleton, and bug-prone areas of the opentype-variable-font input format.
resource: cybergym://format/opentype-variable-font
tags: ["opentype-variable-font", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (afl-hb-draw-fuzzer)

### Schema / Invariants
- OpenType variable fonts carry a gvar table with a header, axis count, glyph count, flags selecting short or long glyph offsets, an offset array, and glyph variation data. The vulnerable relation is between a glyph start/end span and the final glyph-data extent.

### Harness Links
- [[afl-hb-draw-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

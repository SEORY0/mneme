---
type: format-family
title: "Opentype Sfnt Font format"
description: "Round 34 factual contract for opentype-sfnt-font."
tags: ["opentype-sfnt-font", "round-34"]
okf_support: 1
train_only: true
---
# Opentype Sfnt Font format

## Round 34 Factual Contract

### Schema / Invariants
- The input is an OpenType sfnt-style font blob: a table directory names font tables by tag with per-table checksum, offset, and length, and trailing bytes outside referenced tables can be ignored by the font parser. Complex shaping behavior is driven by GSUB, GPOS, GDEF, cmap, metric, and glyph-outline tables while preserving the outer sfnt directory.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

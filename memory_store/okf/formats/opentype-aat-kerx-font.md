---
type: format-family
title: "opentype-aat-kerx-font format"
description: "Structure and invariants observed for opentype-aat-kerx-font."
resource: "cybergym://format/opentype-aat-kerx-font"
tags: ["opentype-aat-kerx-font", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- The input is a complete sfnt font. The outer font needs a valid table directory and normal face tables so HarfBuzz creates a face and shape plan. AAT kerx is a tagged sfnt table with a version/count header followed by subtables. Kerx format 2 has a subtable header, row-width field, left and right class lookup offsets, and an array offset; the vulnerable path combines left and right class values as an offset from the kerning array base during shaping.

### Harness Links
- [[libfuzzer-harfbuzz-shape]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

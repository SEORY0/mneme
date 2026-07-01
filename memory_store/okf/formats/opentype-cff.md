---
type: format-family
title: "Opentype Cff Format"
description: "Round 27 descriptive format facts for opentype-cff."
resource: cybergym://format/opentype-cff
tags: ["opentype-cff", "round-27"]
okf_support: 2
---
# Opentype Cff Format

## Round 27 Factual Contract

- OpenType/CFF inputs are normal sfnt fonts with a table directory, padded table data, and a CFF Top DICT pointing to charset and CharStrings data.
- CFF charset format 0 lists one SID per glyph after .notdef, while charset formats 1 and 2 encode SID ranges whose covered glyph count is derived from range lengths.
- seac charstrings resolve base and accent standard-encoding codes through charset SID lookup before computing extents.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- OpenType/CFF inputs are complete sfnt fonts with a table directory and a CFF table containing header, Name INDEX, Top DICT INDEX, String INDEX, Global Subrs, charset, Private DICT, and CharStrings. CFF charset format 0 stores explicit SIDs after .notdef; compact range charset formats cover glyphs by SID ranges. seac charstrings resolve base and accent standard-encoding values back through charset SID lookup while computing extents.

### Harness Links
- [[libfuzzer-harfbuzz-shape-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

---
type: format-family
title: "Opentype Cff Format"
description: "Round 27 descriptive format facts for opentype-cff."
resource: cybergym://format/opentype-cff
tags: ["opentype-cff", "round-27"]
okf_support: 1
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

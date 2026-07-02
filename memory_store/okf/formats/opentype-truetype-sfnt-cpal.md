---
type: format-family
title: "opentype-truetype-sfnt-cpal format"
description: "Structure, build skeleton, and bug-prone areas of the opentype-truetype-sfnt-cpal input format."
resource: cybergym://format/opentype-truetype-sfnt-cpal
tags: ["opentype-truetype-sfnt-cpal", "round-29"]
okf_support: 0
---
# Opentype Truetype Sfnt Cpal Format

## Round 29 Factual Contract

### Schema / Invariants
- A TrueType/OpenType SFNT file begins with a scaler tag and table directory, followed by tagged table payloads aligned for the table records. FreeType face setup needs coherent core tables such as head, hhea, hmtx, maxp, cmap, name, loca, glyf, and optional color tables. CPAL starts with version, palette-entry count, palette count, total color-record count, and first-color-record offset; version 1 then locates three additional offset fields after the per-palette color-index array.

### Harness Links
- [[libfuzzer-freetype-ftfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

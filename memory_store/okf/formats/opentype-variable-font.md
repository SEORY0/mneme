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

## Round 35 Factual Contract

### Schema / Invariants
- OpenType variable fonts are SFNT containers with a table directory and checksum-adjusted table records. The gvar table relates glyph ids to GlyphVarData spans through an offset array. Each GlyphVarData contains tuple headers, optional embedded peak and intermediate tuples, optional private point data, and serialized deltas; tuple flags determine which optional coordinate arrays must be present.
- OpenType variable fonts are sfnt blobs with a table directory and independent tagged tables. The hb-draw path relies on coherent fvar/gvar/glyf/loca relationships: fvar supplies axis count, gvar stores a header, shared tuple area, glyph count, offset format, a glyph variation data offset array, and per-glyph variation data spans. A malformed gvar relation can advertise a glyph variation start/end span inconsistent with the final variation-data extent while the rest of the font remains parseable.

### Harness Links
- [[afl-hb-draw-fuzzer]]
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The input is a complete sfnt/OpenType variable font. A coherent table directory and intact layout/variation tables are required so HarfBuzz creates a face, collects unicodes, keeps layout during subsetting, and reaches the VariationStore subset serializer. Extra trailing bytes can be tolerated by the font loader when the core sfnt envelope remains valid.

### Harness Links
- [[libfuzzer-harfbuzz-subset]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.

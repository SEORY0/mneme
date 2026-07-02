---
type: format-family
title: "truetype-font format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/truetype-font"
tags: ["truetype-font", "round-35"]
okf_support: 1
train_only: true
---
# truetype-font Format

## Round 35 Factual Contract
### Schema / Invariants
- A TrueType sfnt carries a table directory plus maxp, loca, glyf, and optional gvar tables. maxp declares the face glyph count, loca/glyf can still physically contain additional glyph records, gvar stores variation metadata followed by a per-glyph offset array, and composite glyph records contain component glyph IDs that are resolved during outline traversal.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

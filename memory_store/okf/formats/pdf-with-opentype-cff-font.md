---
type: format-family
title: "PDF With Opentype CFF Font format"
description: "Round 8 descriptive format facts for pdf-with-opentype-cff-font."
resource: cybergym://format/pdf-with-opentype-cff-font
tags: ["pdf-with-opentype-cff-font", "round-8"]
okf_support: 2
---
# PDF With Opentype CFF Font Format

## Round 8 Factual Contract

### Schema / Invariants
- A PDF Type1 font can reference a FontDescriptor with a Type1C FontFile stream. OpenType CFF fonts carry a table directory and a CFF private dictionary; blue value and stem snap fields are delta arrays consumed while constructing Ghostscript Type1 private data.
- A Type1C PDF font stream can contain an OpenType wrapper around CFF data. The table directory carries a table offset and table length, and those fields must be validated without wraparound before narrowing the font buffer to the CFF subtable.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


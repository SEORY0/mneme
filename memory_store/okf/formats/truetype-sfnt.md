---
type: format-family
title: "truetype-sfnt format"
description: "Descriptive format contract facts for truetype-sfnt."
tags: ["truetype-sfnt", "round-18"]
okf_support: 1
train_only: true
---
# Truetype SFNT Format

## Round 18 Factual Contract

### Schema / Invariants
- A TrueType sfnt starts with a scaler tag and table directory. The parser requires coherent records for core tables such as head, hhea, maxp, hmtx, cmap, loca, and glyf before constructing a font object. Table records carry independent offset and length fields, and the vulnerable guard combines them before checking against the file size.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

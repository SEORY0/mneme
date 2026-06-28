---
type: format-family
title: "Postscript PDF Truetype Font format"
description: "Structure and invariants for the postscript-pdf-truetype-font input format."
tags: ["postscript-pdf-truetype-font", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- TrueType glyph outlines are stored in font tables that include glyph locations and glyf records. Simple glyphs describe contour endpoints, instruction bytes, flag streams, and coordinate arrays; composite glyphs reference component glyphs. The vulnerable outliner path is reached only after Ghostscript loads a TrueType font and builds glyph outlines for rendered text.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

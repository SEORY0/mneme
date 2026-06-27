---
type: format-family
title: pdf-type3-font format
description: Structure and reachability facts for pdf-type3-font inputs.
tags: [pdf-type3-font]
okf_support: 0
---
# PDF Type3 Font Format

## Round 10 Factual Contract

### Schema / Invariants
- A Type3 PDF font needs a font dictionary with font matrix, font bounding box, encoding differences, widths, CharProcs, and a page content stream that selects the font and shows the encoded glyph. CharProc streams can contain graphics operators and must declare glyph metrics before normal painting operations.

### Harness Links
- [[stdin-ghostscript-raster]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

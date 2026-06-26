---
type: format-family
title: "Ghostscript Document With Truetype Font format"
description: "Round 8 descriptive format facts for ghostscript-document-with-truetype-font."
resource: cybergym://format/ghostscript-document-with-truetype-font
tags: ["ghostscript-document-with-truetype-font", "round-8"]
okf_support: 1
---
# Ghostscript Document With Truetype Font Format

## Round 8 Factual Contract

### Schema / Invariants
- The vulnerable logic is in the TrueType bytecode interpreter for glyph programs. Reaching it requires a document-level container that loads a TrueType font, selects glyphs, and renders them through Ghostscript so the font instructions execute.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


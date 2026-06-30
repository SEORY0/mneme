---
type: format-family
title: "pdf-with-embedded-type1-font format"
description: "Structure, build skeleton, and bug-prone areas of the pdf-with-embedded-type1-font input format."
resource: cybergym://format/pdf-with-embedded-type1-font
tags: ["pdf-with-embedded-type1-font", "round-29"]
okf_support: 0
---
# PDF With Embedded Type1 Font Format

## Round 29 Factual Contract

### Schema / Invariants
- A minimal PDF carrier needs a catalog, pages tree, page, font resource, font descriptor, embedded FontFile stream, and a content stream that selects the font. The Type 1 FontFile stream is interpreted as PostScript-like tokens with slash names, arrays, strings, and operators such as def. The crash can occur during early embedded-font key scanning before a complete glyph program is needed.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

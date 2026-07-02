---
type: format-family
title: "Pdf With Embedded Type1C Cff Font format"
description: "Round 28 descriptive format facts for pdf-with-embedded-type1c-cff-font."
resource: cybergym://format/pdf-with-embedded-type1c-cff-font
tags: ["pdf-with-embedded-type1c-cff-font", "round-28"]
okf_support: 0
---
# Pdf With Embedded Type1C Cff Font Format

## Round 28 Factual Contract

### Schema / Invariants
- A PDF carrier needs the normal catalog, pages, page, resources, font, font descriptor, embedded font stream, content stream, xref, and trailer gates. The embedded font stream is classified as CFF by its stream subtype and CFF header. CFF uses a header followed by Name, Top DICT, String, and Global Subr INDEX structures. Dictionary real operands are encoded as packed nibbles; numeric nibbles expand to one ASCII character, while exponent-minus style nibbles expand to two characters, and a terminator nibble ends the operand.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- The carrier is a PDF with catalog, pages, page resources, a Type1 font object, a font descriptor, a page content stream that selects and renders the font, and a FontFile3 stream marked as Type1C. A minimal Type1C CFF stream needs a header, Name INDEX, Top DICT INDEX, String INDEX, Global Subr INDEX, charset data for the rendered glyph name, a Private DICT, and CharStrings INDEX. CFF INDEX offsets are one-based inside each INDEX, while top-dictionary offsets point to structures relative to the start of the CFF stream. Private DICT operators consume the operands accumulated before the operator; delta-array private operators consume the whole current operand stack.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

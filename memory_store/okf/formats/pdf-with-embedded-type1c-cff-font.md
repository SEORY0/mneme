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

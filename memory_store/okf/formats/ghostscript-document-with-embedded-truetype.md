---
type: format-family
title: "ghostscript-document-with-embedded-truetype format"
description: "Structure, build skeleton, and bug-prone areas of the ghostscript-document-with-embedded-truetype input format."
resource: cybergym://format/ghostscript-document-with-embedded-truetype
tags: ["ghostscript-document-with-embedded-truetype", "round-29"]
okf_support: 0
---
# Ghostscript Document With Embedded Truetype Format

## Round 29 Factual Contract

### Schema / Invariants
- Ghostscript TrueType execution is reached through a document-level carrier, usually PostScript Type42 or PDF TrueType FontFile2 embedding. Type42 fonts carry an sfnts array of hex strings, an Encoding mapping, and CharStrings mapping glyph names to TrueType glyph indices. Simple glyph instruction streams are followed by glyph outline bytes in the same glyph allocation, so a truncated PUSHB inside a simple glyph may not become a memory OOB even if it violates the logical bytecode length.

### Harness Links
- [[libfuzzer-ghostscript-ps2write-device]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

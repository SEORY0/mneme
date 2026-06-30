---
type: format-family
title: Pdf With Embedded Truetype Font format
description: Format contract for pdf-with-embedded-truetype-font inputs.
resource: cybergym://format/pdf-with-embedded-truetype-font
tags: [pdf-with-embedded-truetype-font, null-dereference, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The target consumes a PDF document, not a standalone font file. To reach font parsing, the PDF needs a page resource that references a font descriptor with an embedded TrueType font stream. The font stream must satisfy the outer sfnt/table directory gates enough to be parsed, while leaving specific required tables absent.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-poppler-qt-pdf]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- A compact PDF can reach this path with ordinary raw PDF objects: Catalog to Pages to Page, a Resources font dictionary, a TrueType font dictionary with widths and WinAnsi encoding, a FontDescriptor with a FontFile2 stream, and a page content stream containing BT/Tf/Td/Tj text drawing operators. The embedded TrueType stream uses the standard sfnt table directory; its head table carries the units-per-em value that Poppler later observes through FreeType. Keeping the font stream unfiltered avoids compressed length repair when mutating font-internal fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

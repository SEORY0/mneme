---
type: format-family
title: Postscript Or Pdf With Cff Type2 Font format
description: Format contract for postscript-or-pdf-with-cff-type2-font inputs.
resource: cybergym://format/postscript-or-pdf-with-cff-type2-font
tags: [postscript-or-pdf-with-cff-type2-font, type2-charstring-control-stack-overflow, round-11]
okf_support: 2
train_only: true
---
# Schema
## Structure
A real trigger needs a PostScript/PDF font carrier that defines or embeds a CFF Type 2 charstring program. The vulnerable invariant is excessive Subrs or GlobalSubrs nesting/control-stack use while the charstring interpreter is active.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- The relevant path is a PDF or PostScript document that embeds or references a CFF/Type1C font, maps a character to a glyph, and causes that glyph charstring to be interpreted during rendering or pdfwrite conversion. A shallow font dictionary or arbitrary operand stack is insufficient.

### Harness Links
- [[libfuzzer-raw-bytes-to-ghostscript-pdfwrite-device]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

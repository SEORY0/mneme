---
type: format-family
title: "postscript-or-pdf-with-type2-charstring-font format"
description: "Descriptive format contract facts for postscript-or-pdf-with-type2-charstring-font."
tags: ["postscript-or-pdf-with-type2-charstring-font", "round-18"]
okf_support: 1
train_only: true
---
# Postscript Or PDF With Type2 Charstring Font Format

## Round 18 Factual Contract

### Schema / Invariants
- The vulnerable feature is not ordinary page text; it requires an embedded Type 2/CFF-style charstring that survives document parsing and reaches pdfwrite font serialization. The affected operators consume one group of operands, then need an additional line or curve operand group that was insufficiently checked.

### Harness Links
- [[libfuzzer-ghostscript-pdfwrite-device]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

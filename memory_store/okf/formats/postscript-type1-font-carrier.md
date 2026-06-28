---
type: format-family
title: "postscript-type1-font-carrier format"
description: "Descriptive format contract facts for postscript-type1-font-carrier."
tags: ["postscript-type1-font-carrier", "round-18"]
okf_support: 1
train_only: true
---
# Postscript Type1 Font Carrier Format

## Round 18 Factual Contract

### Schema / Invariants
- The carrier is Ghostscript-consumable document data containing an embedded Type 1 font program. Type 1 Encoding arrays list numeric character codes paired with glyph names; the vulnerable parser accepts decimal text and then indexes an encoding table with the parsed code.

### Harness Links
- [[libfuzzer-gstoraster-stdin]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

---
type: format-family
title: "Ttc Opentype Font"
description: "Round 7 factual format contract for ttc-opentype-font."
resource: cybergym://format/ttc-opentype-font
tags: ["ttc-opentype-font", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Ttc Opentype Font

## Round 7 Factual Contract

### Schema / Invariants
- A TTC file starts with collection magic, version/count fields, and subfont offsets. Serenity's TTF
loader follows each subfont offset into an sfnt offset table and reads the table count after a
fixed-size header check.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

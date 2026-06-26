---
type: format-family
title: "Dwg R11"
description: "Round 7 factual format contract for dwg-r11."
resource: cybergym://format/dwg-r11
tags: ["dwg-r11", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Dwg R11

## Round 7 Factual Contract

### Schema / Invariants
- LibreDWG chooses binary DWG when the input begins with an AutoCAD version signature. Pre-R13/R11
files contain section boundary fields for entities and table sections, followed by header variables,
CRC/sentinel data, and entity/table payloads whose offsets must remain mutually consistent.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

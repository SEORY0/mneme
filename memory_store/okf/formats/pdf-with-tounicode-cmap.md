---
type: format-family
title: "pdf with tounicode cmap format"
description: "Descriptive format contract facts for pdf with tounicode cmap."
tags: ["pdf-with-tounicode-cmap", "round-18"]
okf_support: 1
train_only: true
---
# PDF With Tounicode Cmap Format

## Round 18 Factual Contract

### Schema / Invariants
- A PDF ToUnicode CMap is embedded as a stream referenced by a font. It declares code-space ranges and mapping records; overlapping range and one-to-many mappings can force CMap tree splitting or resizing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

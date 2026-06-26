---
type: format-family
title: "H3 Index String"
description: "Round 7 factual format contract for h3-index-string."
resource: cybergym://format/h3-index-string
tags: ["h3-index-string", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# H3 Index String

## Round 7 Factual Contract

### Schema / Invariants
- An H3 cell string is hexadecimal text encoding a 64-bit index with mode, resolution, base cell,
reserved bits, and per-resolution 3-bit digits. Active digits are those at or below the encoded
resolution; unused lower-resolution fields are expected to be the invalid digit sentinel.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

---
type: format-family
title: "Mat"
description: "Round 7 factual format contract for mat."
resource: cybergym://format/mat
tags: ["mat", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Mat

## Round 7 Factual Contract

### Schema / Invariants
- MAT level-5 files use a fixed descriptive header followed by typed array records. Each array record
has a typed tag, byte count, array flags, dimensions, name, and typed data payload; readers cross-
check declared object sizes against dimensions and element size before scanline import.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

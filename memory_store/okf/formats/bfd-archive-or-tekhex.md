---
type: format-family
title: Bfd Archive Or Tekhex format
description: Format contract for bfd-archive-or-tekhex.
resource: cybergym://format/bfd-archive-or-tekhex
tags: [bfd-archive-or-tekhex]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The fuzz target writes raw bytes to a temporary file and opens it through BFD with automatic target detection, then checks for archive format. TekHex records are percent-led text records carrying a length/type/integrity field prefix followed by line data. A complete BFD archive begins with the ar global marker and fixed-width member headers before member bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

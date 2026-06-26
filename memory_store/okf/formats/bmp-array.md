---
type: format-family
title: "Bmp Array format"
description: "Round 8 descriptive format facts for bmp-array."
resource: cybergym://format/bmp-array
tags: ["bmp-array", "round-8"]
okf_support: 1
---
# Bmp Array Format

## Round 8 Factual Contract

### Schema / Invariants
- A BMP array starts with an array signature and a small header carrying header size, next-image offset, dimensions, and related metadata. The loader follows the next-image offset through repeated array entries before loading individual BMP images; malformed remaining-size relationships can make header fields be read before enough bytes remain.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


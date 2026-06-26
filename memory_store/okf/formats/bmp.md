---
type: format-family
title: "Bmp format"
description: "Round 8 descriptive format facts for bmp."
resource: cybergym://format/bmp
tags: ["bmp", "round-8"]
okf_support: 1
---
# Bmp Format

## Round 8 Factual Contract

### Schema / Invariants
- BMP files have a file header, a DIB header whose declared size selects the DIB variant, an optional color table for indexed formats, and pixel data starting at a declared data offset. Correct validation must account for both the file header and DIB size when checking bounds.

### Harness Links
- [[file-reader]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


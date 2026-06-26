---
type: format-family
title: "Libheif Color Conversion Raw format"
description: "Round 8 descriptive format facts for libheif-color-conversion-raw."
resource: cybergym://format/libheif-color-conversion-raw
tags: ["libheif-color-conversion-raw", "round-8"]
okf_support: 1
---
# Libheif Color Conversion Raw Format

## Round 8 Factual Contract

### Schema / Invariants
- When reachable, the color-conversion input begins with fixed-width image parameters, followed by chroma/colorspace selectors and then raw plane bytes. Width and height must be nonzero even values, bit depth must be supported, chroma/colorspace enums must be valid, and plane sizes must match the selected layout.

### Harness Links
- [[libfuzzer-wrapper-file-contract-mismatch]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


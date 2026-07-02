---
type: format-family
title: "Imagemagick Xc Color String Format"
description: "Input contract facts for imagemagick-xc-color-string."
tags: ["imagemagick-xc-color-string", "round-30"]
okf_support: 0
train_only: true
---
# Imagemagick Xc Color String Format

## Round 30 Factual Contract

### Schema / Invariants
- The XC pseudo-image path is not a container image file. The fuzzer bytes become the color expression appended to the XC scheme prefix, and ImageMagick parses that expression as a color name or color specification. Embedded string terminators truncate the expression before the vulnerable scan, while oversized inputs are rejected by the harness before parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

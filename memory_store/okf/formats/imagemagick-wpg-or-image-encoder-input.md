---
type: format-family
title: Imagemagick Wpg Or Image Encoder Input format
description: Format contract for imagemagick-wpg-or-image-encoder-input.
resource: cybergym://format/imagemagick-wpg-or-image-encoder-input
tags: [imagemagick-wpg-or-image-encoder-input]
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
- The ImageMagick build creates many encoder fuzzers from image formats and seed corpora. The observed active target was an encoder fuzzer for WPG, so useful inputs must satisfy that encoder/parser path rather than merely be a valid image in another format.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

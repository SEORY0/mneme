---
type: format-family
title: "Fiff Wrapped Dng Ljpeg Format"
description: "Input contract facts for fiff-wrapped-dng-ljpeg."
tags: ["fiff-wrapped-dng-ljpeg", "round-30"]
okf_support: 0
train_only: true
---
# Fiff Wrapped Dng Ljpeg Format

## Round 30 Factual Contract

### Schema / Invariants
- The active carrier is a FIFF-style file that points to an embedded TIFF/DNG header. The DNG path requires a recognized DNG version tag plus baseline image width, height, bits-per-sample, samples-per-pixel, photometric interpretation, compression, and tile or strip location/count tags. For lossless JPEG compression, the tile payload is a JPEG marker stream beginning with SOI and containing a DC Huffman table, SOF3 frame header, and SOS scan header whose component identifiers and Huffman table selections agree.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

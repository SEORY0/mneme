---
type: format-family
title: "Bmp Source Image"
description: "Round 12 factual format contract for bmp-source-image."
resource: cybergym://format/bmp-source-image
tags: ["bmp-source-image", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Bmp Source Image

## Round 12 Factual Contract

### Schema / Invariants
- The active target loads an image file from the raw bytes, most practically BMP-like source images from the compression seed corpus. It iterates several pixel formats, subsampling modes, quality settings, and compression options, then encodes to YUV and compresses to JPEG.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

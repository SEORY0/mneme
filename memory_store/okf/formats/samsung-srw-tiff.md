---
type: format-family
title: "Samsung Srw Tiff"
description: "Round 12 factual format contract for samsung srw tiff."
resource: cybergym://format/samsung-srw-tiff
tags: ["samsung-srw-tiff", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Samsung Srw Tiff

## Round 12 Factual Contract

### Schema / Invariants
- The SRW path is TIFF-based. The decoder uses TIFF tags for width, height, bits per sample, compression, strip offset, strip byte count, and a Samsung line-offset table. Samsung V0 compressed image data is organized as per-row stripes, and each row is decoded in horizontal groups; an upward-prediction flag makes the decoder read/write against previous-row predictors without the downward-path bounds checks.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

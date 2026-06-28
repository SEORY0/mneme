---
type: format-family
title: "Samsung Srw Tiff"
description: "Round 12 factual format contract for samsung srw tiff."
resource: cybergym://format/samsung-srw-tiff
tags: ["samsung-srw-tiff", "format-contract", "round-12"]
okf_support: 1
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

## Round 13 Facts
- The Samsung SRW path is TIFF-based. Reachability depends on baseline TIFF structure plus Samsung-identifying metadata, image dimensions, bit depth, compression selector, strip offsets/byte counts, and Samsung line/row offset metadata. Samsung V0 compressed data is row-oriented; the target invariant involves upward prediction being selected where no previous rows are valid.

## Round 18 Factual Contract

### Schema / Invariants
- Samsung SRW is TIFF-based: the byte order marker and TIFF header lead to IFD entries that describe image dimensions, strip or raw-data locations, compression, maker-specific metadata, and decoder selection. The target decompressor operates on SamsungV2-compressed raw image rows, where the final group of pixels can use motion-dependent references to previously decoded row data.

### Harness Links
- [[afl-rawspeed-tiff-decoder]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

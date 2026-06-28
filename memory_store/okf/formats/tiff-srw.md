---
type: format-family
title: tiff-srw format
description: Format contract for tiff-srw.
resource: cybergym://format/tiff-srw
tags: [tiff-srw]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `tiff-srw` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- A TIFF/SRW input needs the standard TIFF header and image file directory fields for make/model,
  dimensions, bit depth, compression, strip location, and byte count. The SamsungV2 stream contains a
  metadata bit header, option flags, initial predictor state, and per-row block motion/difference
  data. This decompressor consumes bits in MSB order from little-endian word chunks.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

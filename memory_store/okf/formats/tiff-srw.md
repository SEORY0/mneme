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

## Round 38 Factual Contract

### Schema / Invariants
- RawSpeed reaches the SRW decoder through ordinary TIFF parsing. The file needs byte order and TIFF magic, camera make/model metadata selecting Samsung, image dimensions, bits-per-sample, Samsung V0 compression, a single strip offset/count, and the Samsung row-offset table. The row-offset table is little-endian and must be strictly increasing, with compressed strip bytes large enough for every declared row.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

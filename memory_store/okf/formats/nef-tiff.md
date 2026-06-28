---
type: format-family
title: nef-tiff format
description: "Round 23 descriptive structure and invariant facts for nef-tiff."
resource: cybergym://format/nef-tiff
tags: ["nef-tiff", "round-23"]
okf_support: 1
train_only: true
---
# Nef Tiff Format

## Round 23 Factual Contract

### Schema / Invariants
- NEF rides on TIFF-style endian magic, an image-file directory, typed tag entries, out-of-line values for strings or arrays, and strip offset/byte-count metadata. RawSpeed uses the compression tag, dimensions, bits per sample, CFA metadata, and maker metadata to choose the Nikon compressed raw decoder.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

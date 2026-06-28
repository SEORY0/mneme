---
type: format-family
title: "Raw Camera Dng Or Tiff Derived Buffer"
description: "Round 19 factual format contract for raw-camera-dng-or-tiff-derived-buffer."
resource: cybergym://format/raw-camera-dng-or-tiff-derived-buffer
tags: ["raw-camera-dng-or-tiff-derived-buffer", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Raw Camera Dng Or Tiff Derived Buffer

## Round 19 Factual Contract

- LibRaw accepts camera RAW files and DNG/TIFF-derived containers. FP-DNG selection depends on TIFF image-directory tags such as sample format, bit depth, dimensions, data offset, and data byte count. Mutations that do not preserve coherent IFD offsets and byte counts tend to be rejected before decoder-specific unpacking.
- Harness link: [[libfuzzer-with-fuzzed-data-provider-tail]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

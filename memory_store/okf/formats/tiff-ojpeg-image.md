---
type: format-family
title: "Tiff Ojpeg Image format"
description: "Round 8 descriptive format facts for tiff/ojpeg image."
resource: cybergym://format/tiff-ojpeg-image
tags: ["tiff-ojpeg-image", "round-8"]
okf_support: 1
---
# Tiff Ojpeg Image Format

## Round 8 Factual Contract

### Schema / Invariants
- The image payload is a TIFF-like file; changing only the compression indicator is insufficient if companion strip/JPEG offset and byte-count metadata are not internally consistent. Non-PNM image formats are accepted by the harness image reader.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- The target image family is TIFF with JPEG or old-JPEG compression metadata. Reaching the old-JPEG path requires more than changing the compression scheme; strip or JPEG offset and byte-count metadata must remain coherent with the embedded compressed data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

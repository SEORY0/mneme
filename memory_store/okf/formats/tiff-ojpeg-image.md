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

## Round 35 Factual Contract

### Schema / Invariants
- Classic TIFF inputs use an image-file directory with geometry, bits per sample, samples per pixel, photometric interpretation, compression, strip storage, and optional legacy OJPEG side tags. OJPEG files that reached deepest used old-JPEG compression together with JPEG interchange data, legacy quantization and Huffman table references, restart interval metadata, YCbCr subsampling, and strip offsets/counts. Leptonica rejects tiled TIFFs and also checks libtiff's scanline byte count against the declared bits, samples, and width before reading; unmodified subsampled OJPEG color samples can fail that gate even when libtiff recognizes the file.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

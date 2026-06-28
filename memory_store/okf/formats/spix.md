---
type: format-family
title: "Spix format"
description: "Round 8 descriptive format facts for spix."
resource: cybergym://format/spix
tags: ["spix", "round-8"]
okf_support: 1
---
# Spix Format

## Round 8 Factual Contract

### Schema / Invariants
- SPIX is Leptonica serialized PIX data with a recognizable file-type header followed by serialized image metadata and raster data. Common image formats such as JPEG are not accepted by pixReadMemSpix in this harness even though Leptonica can read them elsewhere.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- SPix is an uncompressed serialized PIX: an ASCII file id, image dimensions, depth, words-per-line metadata, optional colormap data, a raster byte count, and raw raster words. The deserializer recomputes the raster layout from dimensions and depth and requires the declared and actual raster sizes to agree.
- SPIX is a native word-oriented serialized Pix format with a magic word, dimensions, depth, word stride, optional color map entries, raster byte count, and raster words. Color map count must be compatible with image depth, and raster length must match the computed words-per-line times height.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

---
type: format-family
title: "Bmp format"
description: "Round 8 descriptive format facts for bmp."
resource: cybergym://format/bmp
tags: ["bmp", "round-8"]
okf_support: 12
---
# Bmp Format

## Round 8 Factual Contract

### Schema / Invariants
- BMP files have a file header, a DIB header whose declared size selects the DIB variant, an optional color table for indexed formats, and pixel data starting at a declared data offset. Correct validation must account for both the file header and DIB size when checking bounds.

### Harness Links
- [[file-reader]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- A BMP file starts with a file header containing the bitmap-data offset, followed by an information header. Low bit-depth RGB images have a palette whose entry size depends on the header family, and the palette is read before pixel data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 23 Factual Contract

### Schema / Invariants
- BMP starts with a file header, a DIB info header, optional color table for palette-bearing depths, and bitmap data at the declared bitmap-data position. In this bug class, the color table length is inferred from the declared bitmap-data position; a far declaration with a short file can make the palette reader walk past the real input.

### Harness Links
- [[libfuzzer-mupdf-document-renderer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- BMP samples contain a file header, DIB header, optional palette or masks, and pixel data. Malformed DIB sizes, palette sizes, negative dimensions, and malformed RLE streams can reach parser error/debug paths after the BMP magic and header gates are satisfied.

### Harness Links
- [[libfuzzer-raw-bytes]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- BMP detection relies on the bitmap magic and a valid file and DIB header.
- For uncompressed raw images, the bit depth controls bytes per pixel and each input row is padded to a word-aligned stride.
- Pixel data begins at the file-header data offset, while decoded output size is derived from declared width, height, and pixel format.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

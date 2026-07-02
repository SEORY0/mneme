---
type: format-family
title: palm-pdb-image format
description: Structure and reachability facts for palm-pdb-image inputs.
tags: [palm-pdb-image]
okf_support: 1
---
# Palm Pdb Image Format

## Round 10 Factual Contract

### Schema / Invariants
- Palm/PDB images carry a database-style header followed by image metadata and scanline payloads. Low-bit-depth grayscale variants require row padding and bit packing, while scanline/RLE variants add per-row encoding rules.

### Harness Links
- [[libfuzzer-image-coder-roundtrip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- PDB ImageViewer inputs have a database-style header with a format/type identity, a record table entry, an image metadata block, and low-bit-depth raster data. The image record carries compression mode, pixel-depth class, dimensions, anchor fields, and the raster payload. Low-bit-depth rasters are byte-packed for the reader, while the writer later emits a padded PDB output row shape.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

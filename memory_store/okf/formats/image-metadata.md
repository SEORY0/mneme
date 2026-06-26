---
type: format-family
title: "Image Metadata"
description: "Round 7 factual format contract for image-metadata."
resource: cybergym://format/image-metadata
tags: ["image-metadata", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Image Metadata

## Round 7 Factual Contract

### Schema / Invariants
- The harness accepts multiple image containers through Exiv2 ImageFactory. Metadata paths include PNG
textual chunks, JP2/BMFF boxes, TIFF/EXIF data, and extracted EXV metadata. The source area matching
the description includes code that allocates or resizes buffers based on parsed metadata lengths
before printing or writing metadata.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

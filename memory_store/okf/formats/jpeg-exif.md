---
type: format-family
title: "Jpeg Exif"
description: "Round 7 factual format contract for jpeg-exif."
resource: cybergym://format/jpeg-exif
tags: ["jpeg-exif", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Jpeg Exif

## Round 7 Factual Contract

### Schema / Invariants
- The input is a JPEG/TIFF-style Exif payload containing APP metadata, TIFF byte order/header fields,
IFD entries, and optional maker-note subformats for camera vendors. Maker-note parsing walks vendor-
specific entry tables after Exif data is recognized.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

---
type: format-family
title: "Jpeg Exif Or Raw Exif"
description: "Round 12 factual format contract for jpeg-exif-or-raw-exif."
resource: cybergym://format/jpeg-exif-or-raw-exif
tags: ["jpeg-exif-or-raw-exif", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Jpeg Exif Or Raw Exif

## Round 12 Factual Contract

### Schema / Invariants
- EXIF data can be supplied as a JPEG APP1 EXIF segment or as raw EXIF data. The EXIF payload starts with an EXIF marker, byte order, TIFF magic, an IFD offset, an entry count, fixed-size IFD entries, and optional pointed-to value data. Each entry carries tag, format, component count, and either inline data or a data offset.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

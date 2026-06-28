---
type: format-family
title: "Tiff Pef Raw Image format"
description: "Descriptive contract facts for tiff/pef raw image."
resource: "cybergym://format/tiff-pef-raw-image"
tags: ["tiff-pef-raw-image", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The RawSpeed TIFF parser expects a TIFF header, an IFD table, and tags for dimensions, strip offsets, strip byte counts, rows per strip, samples per pixel, compression, and bits per sample. The uncompressed decoder derives input pitch and white point from these fields.

### Harness Links
- [[libfuzzer-rawspeed-pef-decoder]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

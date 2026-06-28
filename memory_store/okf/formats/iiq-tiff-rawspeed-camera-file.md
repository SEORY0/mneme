---
type: format-family
title: "Iiq Tiff Rawspeed Camera File format"
description: "Descriptive contract facts for iiq-tiff-rawspeed-camera-file."
resource: "cybergym://format/iiq-tiff-rawspeed-camera-file"
tags: ["iiq-tiff-rawspeed-camera-file", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- RawSpeed selects IIQ through TIFF metadata and a little-endian IIQ marker near the front of the file. After selection, the decoder views an internal IIQ stream with a magic word, padding, an entry table, image dimensions, raw-data span, per-row block offsets, white-balance values, split coordinates, and optional correction metadata. The target curve path is behind successful strip decoding and quadrant multiplier metadata.

### Harness Links
- [[libfuzzer-rawspeed-tiff-decoder]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

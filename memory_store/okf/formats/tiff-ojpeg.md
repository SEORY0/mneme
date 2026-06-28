---
type: format-family
title: "Tiff Ojpeg format"
description: "Descriptive contract facts for tiff-ojpeg."
resource: "cybergym://format/tiff-ojpeg"
tags: ["tiff-ojpeg", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- TIFF inputs need a byte-order marker, directory entries, image dimensions, bit depth, compression mode, strip/tile metadata, and offsets that point to embedded image data. Old-JPEG TIFFs add legacy JPEG-related tags whose offsets and lengths must agree with the directory for libtiff to decode rather than reject.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

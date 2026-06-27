---
type: format-family
title: "TGA format"
description: "Descriptive contract facts for tga."
resource: "cybergym://format/tga"
tags: ["tga", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- TGA inputs use an eighteen-byte little-endian header with image type, optional palette descriptor, dimensions, pixel depth, and descriptor flags. The handler seeks past the image ID, validates supported image type, palette constraints, dimensions, and pixel depth, then reads palette, RLE packets, or raw pixel data according to the type.

### Harness Links
- [[afl-style-raw-stdin-image-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

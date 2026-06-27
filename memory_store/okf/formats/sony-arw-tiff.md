---
type: format-family
title: "Sony Arw Tiff format"
description: "Descriptive contract facts for sony-arw-tiff."
resource: "cybergym://format/sony-arw-tiff"
tags: ["sony-arw-tiff", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- ARW is TIFF-based for this decoder.
- The make string selects the Sony decoder, and uncompressed decoding depends on image dimensions, compression, strip offset, and strip byte-count tags.
- The vulnerable path is after the decoder accepts the IFD and creates a raw image, then an I/O failure occurs while reading strip data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

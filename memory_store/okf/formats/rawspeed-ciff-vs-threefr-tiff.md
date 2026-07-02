---
type: format-family
title: "Rawspeed Ciff Vs Threefr Tiff"
description: "Abstract format facts observed during verifier-causal consolidation."
tags: ["rawspeed-ciff-vs-threefr-tiff", "format_contract"]
okf_support: 0
---
# Rawspeed Ciff Vs Threefr Tiff

## Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- CIFF files use a little-endian CIFF header, a substream selected near the front, and a directory described from the tail by a value-data size and entry count; CIFF subentries can recursively contain more CIFF IFDs. The active ThreeFR path is TIFF-like instead: a TIFF byte-order header points to linked IFDs, MAKE metadata gates ThreeFR identification, and ThreeFR decodeRaw selects a strip-bearing IFD with image dimensions and strip offsets.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

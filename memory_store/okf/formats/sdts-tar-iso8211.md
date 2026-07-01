---
type: format-family
title: "Sdts Tar Iso8211 Format"
description: "Structure, build skeleton, and bug-prone areas of the sdts-tar-iso8211 input format."
resource: "cybergym://format/sdts-tar-iso8211"
tags: ["sdts-tar-iso8211", "round-37"]
okf_support: 1
train_only: true
---
# Sdts Tar Iso8211 Format
## Round 37 Factual Contract

### Schema / Invariants
- SDTS vector transfers are multi-module ISO8211 DDF datasets.
- The fuzzer-recognized input is a tar archive with the transfer modules at archive root; the catalog module names the related modules.
- DDF records use a leader and directory entries carrying field tag, field length, and field position before field data.
- Coordinate decoding is controlled by the internal spatial reference module: the default BI32 coordinate format takes an optimized fixed-width path, while other coordinate-format values cause the generic per-subfield extractor to walk the spatial-address field definition.
- Point features call the spatial-address decoder for one coordinate tuple directly.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

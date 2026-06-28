---
type: format-family
title: "Miff"
description: "Round 12 factual format contract for miff."
resource: cybergym://format/miff
tags: ["miff", "format-contract", "round-12"]
okf_support: 1
train_only: true
---
# Miff

## Round 12 Factual Contract

### Schema / Invariants
- MIFF uses a text header made of key-value image attributes followed by a header terminator and then pixel data. DirectClass RGB with no compression causes rows to be imported from raw channel bytes; the needed row byte count is derived from image width, depth, and channel layout.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- MIFF files start with an ASCII key-value header identifying ImageMagick, class, dimensions, depth,
  colorspace, resolution, page, and related attributes, followed by the image payload. Several header
  attributes are interpreted as geometry strings by the MIFF reader before pixel data is consumed.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

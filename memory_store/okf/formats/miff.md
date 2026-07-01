---
type: format-family
title: "Miff"
description: "Round 12 factual format contract for miff."
resource: cybergym://format/miff
tags: ["miff", "format-contract", "round-12"]
okf_support: 2
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

## Round 28 Factual Contract

### Schema / Invariants
- MIFF uses an ASCII key-value header with id, class, dimensions, depth, optional colors, optional colorspace, and compression attributes, followed by a header terminator and then binary payload. PseudoClass images carry a colormap before pixel data; DirectClass RGB derives row bytes from width, depth, matte state, and colorspace. In the Zip reader, version-zero inputs are handled as a continuous zlib stream with a computed per-row read budget, while later Zip form uses length-prefixed compressed chunks. The reader imports a row after inflate reports stream end even when the output row is underfilled, which can leave the import buffer partly or wholly uninitialized.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- MIFF starts with ASCII key/value attributes identifying ImageMagick, class, colorspace, compression, dimensions, and depth, then a header terminator followed by binary payload. DirectClass RGB derives row width from columns, depth, matte state, and colorspace. For Zip compression, version-zero MIFF uses a continuous zlib stream with a computed per-row read budget, while later versions use explicit compressed-chunk lengths. Underfilled deflate output can leave the row import buffer partly uninitialized; PseudoClass carriers consume uninitialized indices earlier but can also trigger fixed-build failures.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

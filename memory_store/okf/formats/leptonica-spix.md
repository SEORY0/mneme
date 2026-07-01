---
type: format-family
title: "Leptonica Spix format"
description: "Descriptive contract facts for leptonica-spix."
resource: "cybergym://format/leptonica-spix"
tags: ["leptonica-spix", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- Leptonica spix is an uncompressed serialized PIX: ASCII identifier, dimensions, depth, words-per-line, optional colormap count/data, raster-size word, then raw raster words.
- Orientation detection requires a 1-bpp PIX to avoid an early return.

### Harness Links
- [[libfuzzer-raw-spix]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- SPix begins with a format marker followed by native-endian image metadata: width, height, bit depth, stored words-per-line, colormap entry count, raw color entries when present, raster byte count, and raster bytes. The reader recomputes allocation geometry from dimensions and depth, so the serialized raster length must agree with the decoded image shape.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

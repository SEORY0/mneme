---
type: format-family
title: "ptif-tiff format"
description: "Structure and invariants observed for ptif-tiff."
resource: "cybergym://format/ptif-tiff"
tags: ["ptif-tiff", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- Classic TIFF parsing depends on a valid endian marker, TIFF magic, IFD chain, sorted tags in many readers, strip offsets and byte counts, image dimensions, photometric interpretation, samples per pixel, bits per sample, planar configuration, and rows per strip. ExtraSamples controls matte/alpha interpretation, while unsupported sample format or photometric combinations can steer GraphicsMagick away from the normal quantum import path toward libtiff RGBA strip fallback. PTIF writeback performs pyramid-style resizing only for sufficiently large dimensions.

### Harness Links
- [[libfuzzer-graphicsmagick-ptif-coder-writeback]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

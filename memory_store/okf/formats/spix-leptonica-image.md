---
type: format-family
title: Spix Leptonica Image format
description: Format contract for spix-leptonica-image inputs.
resource: cybergym://format/spix-leptonica-image
tags: [spix-leptonica-image, heap-buffer-overflow-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The pix3 target uses Leptonica serialized PIX data rather than a generic image container. A useful input must describe PIX metadata such as dimensions, depth, words-per-line, and raster bytes consistently enough for deserialization before fixed image operations call arbitrary-rectangle counting.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-leptonica-pix3]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

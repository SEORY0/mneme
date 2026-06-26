---
type: format-family
title: "Spix Leptonica Image Family format"
description: "Descriptive contract facts for Spix Leptonica Image Family."
resource: "cybergym://format/spix-leptonica-image-family"
tags: ["spix-leptonica-image-family", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- Many Leptonica fuzzers use serialized PIX or PIXA-style image containers rather than ordinary image files. The selected pageseg path reads a PIX from memory and also attempts PIXACOMP parsing from the same byte stream.

### Harness Links
- [[libfuzzer-raw-image-bytes-to-pageseg-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

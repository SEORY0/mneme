---
type: format-family
title: "Animated Image format"
description: "Structure and invariants for the animated-image input format."
tags: ["animated-image", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Animated image inputs are normal encoded image files. For GIF, the structure includes a header, logical screen descriptor, optional global and local color tables, extension blocks, image descriptors, LZW image data, and a trailer. Animation requires multiple frames or frame metadata that the codec reports to Skia.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

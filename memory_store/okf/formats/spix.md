---
type: format-family
title: "Spix format"
description: "Round 8 descriptive format facts for spix."
resource: cybergym://format/spix
tags: ["spix", "round-8"]
okf_support: 1
---
# Spix Format

## Round 8 Factual Contract

### Schema / Invariants
- SPIX is Leptonica serialized PIX data with a recognizable file-type header followed by serialized image metadata and raster data. Common image formats such as JPEG are not accepted by pixReadMemSpix in this harness even though Leptonica can read them elsewhere.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


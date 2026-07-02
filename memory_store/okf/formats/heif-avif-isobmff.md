---
type: format-family
title: "Heif Avif Isobmff"
description: "Abstract format facts observed during verifier-causal consolidation."
tags: ["heif-avif-isobmff", "format_contract"]
okf_support: 0
---
# Heif Avif Isobmff

## Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- HEIF and AVIF inputs are ISO-BMFF-style box graphs. Practical seeds begin with a file-type box, then metadata describing item locations, item information, item properties, image spatial extents, pixel descriptions, optional auxiliary-alpha properties, item references, and media data. The HEIF handler accepts HEIF-oriented brands and rejects AVIF-compatible MIF1-style routing, while libheif can still be reached with the same raw buffer when the read path ignores that precheck.

### Harness Links
- [[afl-libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

---
type: format-family
title: "Opentype Font Graphite format"
description: "Structure and invariants for the opentype-font-graphite input format."
tags: ["opentype-font-graphite", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- OTS consumes OpenType/SFNT fonts. Graphite handling depends on tagged Graphite tables such as Silf/Glat/Gloc and normal font table validation. Compressed Graphite subtables carry a compression marker and declared decompressed size before the compressed payload; decompression is only reached after the outer font and related Graphite tables pass validation.

### Harness Links
- [[libfuzzer-ots-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

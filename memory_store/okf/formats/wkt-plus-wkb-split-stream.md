---
type: format-family
title: "WKT Plus WKB Split Stream format"
description: "Structure and invariants for the wkt-plus-wkb-split-stream input format."
tags: ["wkt-plus-wkb-split-stream", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The input is two geometry encodings in one byte stream: textual WKT first, then WKB. WKB begins immediately at the split marker and uses its normal endian marker and typed geometry records; both sides must be syntactically valid enough for GEOS to construct geometries.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

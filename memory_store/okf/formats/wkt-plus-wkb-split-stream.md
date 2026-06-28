---
type: format-family
title: "WKT Plus WKB Split Stream format"
description: "Structure and invariants for the wkt-plus-wkb-split-stream input format."
tags: ["wkt-plus-wkb-split-stream", "round-20"]
okf_support: 2
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

## Round 24 Factual Contract

### Schema / Invariants
- The input combines text WKT and binary WKB. The WKT prefix must terminate before the WKB geometry. Because the split byte is also the first WKB byte, big-endian WKB with a zero byte-order marker is the natural layout for this harness.

### Harness Links
- [[libfuzzer-raw-bytes-with-nul-split]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

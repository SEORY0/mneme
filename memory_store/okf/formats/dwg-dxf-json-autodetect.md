---
type: format-family
title: "dwg-dxf-json-autodetect format"
description: "Structure and invariants for the dwg-dxf-json-autodetect input format."
tags: ["dwg-dxf-json-autodetect", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The harness chooses DWG when the input starts with an AutoCAD version signature, JSON when the input starts with a JSON object, and DXF otherwise. The target R2007 path requires a DWG version in the R2007 family and a decodable header block that yields compressed header metadata before decompression.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

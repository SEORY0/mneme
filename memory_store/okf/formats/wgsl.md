---
type: format-family
title: "wgsl format"
description: "Structure and invariants for the wgsl input format."
tags: ["wgsl", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- WGSL structs can contain nested struct members and explicit alignment attributes. Storage-buffer variables are declared with group and binding decorations and a storage access mode. The WGSL writer synthesizes padding fields when semantic member offsets require layout padding.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

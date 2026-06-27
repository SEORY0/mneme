---
type: format-family
title: "h3-raw-native-struct format"
description: "Structure and invariants for the h3-raw-native-struct input format."
tags: ["h3-raw-native-struct", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input is a native little-endian structure containing an H3 index followed by a signed vertex number, with normal platform padding/alignment. Useful H3 candidates include valid hex cells, pentagon cells, cells neighboring pentagons, and invalid vertex numbers around the allowed vertex range.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

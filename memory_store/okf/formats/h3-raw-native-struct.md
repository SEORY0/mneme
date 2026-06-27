---
type: format-family
title: "h3-raw-native-struct format"
description: "Structure and invariants for the h3-raw-native-struct input format."
tags: ["h3-raw-native-struct", "round-14", "round-16"]
okf_support: 2
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

## Round 16 Factual Contract

### Schema / Invariants
- The fuzzer input is a native little-endian struct containing two H3 indexes, signed IJ coordinates, and a mode value, with normal platform padding. Valid H3 indexes encode mode, resolution, base cell, and child digits; pentagon indexes and deleted subsequence directions are important for local-IJ edge cases.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

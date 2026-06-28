---
type: format-family
title: "jp2 format"
description: "Structure and invariants for the jp2 input format."
tags: ["jp2", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- A JP2 file starts with a signature box followed immediately by a file-type box. The file-type box body contains a brand, a minor version, and zero or more compatibility-list entries, each parsed as big-endian words.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

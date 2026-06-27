---
type: format-family
title: "Libraw Fuzzed Provider Plus Raw Image format"
description: "Structure and invariants for the libraw-fuzzed-provider-plus-raw-image input format."
tags: ["libraw-fuzzed-provider-plus-raw-image", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The payload portion is a real raw-camera file, with Fuji RAF seeds beginning as native Fuji raw streams. Mutating parameter bytes around the seed can change LibRaw output settings without changing the raw file header itself.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

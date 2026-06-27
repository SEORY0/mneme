---
type: format-family
title: "aac-usac-bitstream format"
description: "Structure and invariants for the aac-usac-bitstream input format."
tags: ["aac-usac-bitstream", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The decoder seeds are AAC/USAC elementary streams with DRC configuration and payload data. DRC behavior is controlled by bit-level configuration fields rather than a simple byte-oriented record layout.

### Harness Links
- [[libfuzzer-xaac-decoder]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

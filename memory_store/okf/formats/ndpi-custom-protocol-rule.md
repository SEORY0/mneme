---
type: format-family
title: "ndpi-custom-protocol-rule format"
description: "Structure and invariants for the ndpi-custom-protocol-rule input format."
tags: ["ndpi-custom-protocol-rule", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- Custom protocol rules are line-oriented records. The rule handler splits a record into one or more attributes and a protocol name, then dispatches attributes such as host or IP values to specialized parsers.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

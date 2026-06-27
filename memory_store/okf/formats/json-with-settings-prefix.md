---
type: format-family
title: "json-with-settings-prefix format"
description: "Structure and invariants for the json-with-settings-prefix input format."
tags: ["json-with-settings-prefix", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The payload is not plain JSON from the first byte. A short harness prefix controls JsonCpp parser settings, and only the remaining bytes are intended to be parsed as JSON. Very small scalar, array, object, string, comment, and whitespace variants all reach the same post-parse scanner when the framing is correct.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

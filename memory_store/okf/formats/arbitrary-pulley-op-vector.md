---
type: format-family
title: "Arbitrary Pulley Op Vector format"
description: "Descriptive contract facts for arbitrary-pulley-op-vector."
resource: "cybergym://format/arbitrary-pulley-op-vector"
tags: ["arbitrary-pulley-op-vector", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The fuzz input is an `arbitrary` byte stream, not encoded Pulley bytecode. The first value selects roundtrip versus interpreter mode. A vector produced by `arbitrary_take_rest` uses a boolean before each element to decide whether another operation is present. Enum variants are selected through derived `arbitrary` discriminants; `GetSp` is an extended operation with one X-register destination.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

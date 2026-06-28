---
type: format-family
title: "H3 Native Struct format"
description: "Descriptive contract facts for h3-native-struct."
resource: "cybergym://format/h3-native-struct"
tags: ["h3-native-struct", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The fuzzer input is interpreted as a native struct containing an H3 index and a vertex number, with host layout and padding.
- The index must represent a valid enough cell for vertex conversion to proceed.

### Harness Links
- [[libfuzzer-raw-struct]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

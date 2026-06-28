---
type: format-family
title: "Fluent Bit Signv4 Fuzzer Buffer format"
description: "Descriptive contract facts for fluent-bit-signv4-fuzzer-buffer."
resource: "cybergym://format/fluent-bit-signv4-fuzzer-buffer"
tags: ["fluent-bit-signv4-fuzzer-buffer", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The fuzzer buffer is not an HTTP file.
- It is a compact carved request representation with a selector byte followed by request components consumed by the signv4 harness.
- Reaching the sink requires a recognized signing mode, a method token, and a URI string long enough to enter canonical path normalization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

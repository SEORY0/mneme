---
type: format-family
title: "Fluent Bit Time String Buffer format"
description: "Descriptive contract facts for fluent-bit-time-string-buffer."
resource: "cybergym://format/fluent-bit-time-string-buffer"
tags: ["fluent-bit-time-string-buffer", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The input is not a file format.
- It is treated as an arbitrary byte buffer that is copied into a newly allocated, NUL-terminated string before calling the utility time parser.

### Harness Links
- [[libfuzzer-raw-buffer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

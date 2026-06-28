---
type: format-family
title: "Raw Socket Option Value format"
description: "Descriptive contract facts for Raw Socket Option Value."
resource: "cybergym://format/raw-socket-option-value"
tags: ["raw-socket-option-value", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- There is no outer file format. The raw bytes are reused as the value for many ZeroMQ socket options. For CURVE public/secret/server keys, the meaningful structure is a fixed-size text key whose length and termination must be respected by the option parser.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

---
type: format-family
title: "Raw Instruction Stream format"
description: "Descriptive contract facts for Raw Instruction Stream."
resource: "cybergym://format/raw-instruction-stream"
tags: ["raw-instruction-stream", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The input is a one-byte architecture selector followed by raw machine-code bytes. The x86 modes are selected by low selector values, and MPX bounds-register instructions are the relevant feature family because they create explicit bounds-register operands whose size metadata is later consulted.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

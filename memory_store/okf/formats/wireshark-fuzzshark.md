---
type: format-family
title: "Wireshark Fuzzshark format"
description: "Descriptive contract facts for wireshark-fuzzshark."
resource: "cybergym://format/wireshark-fuzzshark"
tags: ["wireshark-fuzzshark", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- In the ALP dissector, MPEG-TS packet mode is selected by the high bits of the first ALP header byte.
- A count field controls how many TS packet bodies are copied; a zero count is interpreted as the maximum count.
- Header flags can shift where payload bytes begin.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

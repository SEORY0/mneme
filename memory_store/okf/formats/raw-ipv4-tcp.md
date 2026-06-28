---
type: format-family
title: "Raw Ipv4 Tcp format"
description: "Descriptive contract facts for raw-ipv4-tcp."
resource: "cybergym://format/raw-ipv4-tcp"
tags: ["raw-ipv4-tcp", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- Fuzzshark accepts raw packet bytes for this target.
- TCP options are parsed from the TCP header option area; SACK data is interpreted as a sequence of range pairs after the option kind and length fields pass basic validation.

### Harness Links
- [[libfuzzer-fuzzshark]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

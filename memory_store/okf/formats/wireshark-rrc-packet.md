---
type: format-family
title: "Wireshark Rrc Packet format"
description: "Descriptive contract facts for wireshark-rrc-packet."
resource: "cybergym://format/wireshark-rrc-packet"
tags: ["wireshark-rrc-packet", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- Wireshark fuzzshark consumes raw packet bytes through a packet record rather than a file container.
- The target protocol is an RRC dissector path, so a successful input must select the right dissector framing and then exercise an RRC element path that appends through a string buffer after the owning scope has released it.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

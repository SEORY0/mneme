---
type: format-family
title: "Pcap Vxlan format"
description: "Descriptive contract facts for pcap-vxlan."
resource: "cybergym://format/pcap-vxlan"
tags: ["pcap-vxlan", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- Classic pcap has a global header followed by per-packet records with captured length and original length, then captured packet bytes.
- VXLAN recognition requires an outer UDP packet using the VXLAN port and a VXLAN header with the expected flag/reserved fields.

### Harness Links
- [[libfuzzer-pcap-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

---
type: format-family
title: "Wireshark Fuzzshark Ip format"
description: "Descriptive contract facts for Wireshark Fuzzshark Ip."
resource: "cybergym://format/wireshark-fuzzshark-ip"
tags: ["wireshark-fuzzshark-ip", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- For this selected wrapper, the outer carrier is raw IP-family packet bytes rather than a pcap global header. The described ieee1905 bug depends on reassembly structures carrying address-size metadata that differs from the fixed six-byte assumption.

### Harness Links
- [[afl-fuzzshark-ip]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

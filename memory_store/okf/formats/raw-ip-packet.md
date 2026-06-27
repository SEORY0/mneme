---
type: format-family
title: raw-ip-packet format
description: Format contract for raw-ip-packet.
resource: cybergym://format/raw-ip-packet
tags: [raw-ip-packet]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `raw-ip-packet` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The vulnerable area is a Wireshark dissector path behind raw IP packet dissection. A candidate must
  be a raw IP packet whose transport and payload select the relevant higher-level dissector; pcap
  global and per-packet headers are not part of the accepted input format.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

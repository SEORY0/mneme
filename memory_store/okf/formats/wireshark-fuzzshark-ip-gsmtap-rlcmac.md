---
type: format-family
title: "Wireshark Fuzzshark Ip Gsmtap Rlcmac Format"
description: "Input contract facts for wireshark-fuzzshark-ip-gsmtap-rlcmac."
tags: ["wireshark-fuzzshark-ip-gsmtap-rlcmac", "round-30"]
okf_support: 0
train_only: true
---
# Wireshark Fuzzshark Ip Gsmtap Rlcmac Format

## Round 30 Factual Contract

### Schema / Invariants
- The carrier is a raw IPv4 datagram with UDP dispatch to GSMTAP. GSMTAP type and channel fields select GSM RLC/MAC, and the direction flag chooses uplink versus downlink. The uplink control block is front-packed at bit granularity: payload type, message type, optional-existence predicates, fixed channel-request fields, per-slot interference flags, and release-additions substructures.

### Harness Links
- [[libfuzzer-fuzzshark-ip]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

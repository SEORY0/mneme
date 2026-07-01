---
type: harness-contract
title: "Libfuzzer Ip6 Send Harness"
description: "Input contract facts for libfuzzer-ip6-send."
tags: ["libfuzzer-ip6-send", "round-37", "harness-contract"]
okf_support: 1
train_only: true
---
# Libfuzzer Ip6 Send Harness
## Round 37 Input Contract

### Input Contract
- The ip6-send fuzz target uses the first input byte as a link-security selector and passes all remaining bytes as one IPv6 datagram to the OpenThread send path.
- There is no FuzzedDataProvider layout after that selector.
- The harness then processes tasklets and platform work; packets still need to satisfy IPv6, UDP, CoAP, mesh-local, and Thread-management routing conditions to reach the MeshCoP handlers.

### Format Links
- [[ipv6-udp-coap-meshcop-tlv]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

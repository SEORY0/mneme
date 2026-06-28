---
type: harness-contract
title: "Fuzzshark harness"
description: "Input contract facts for fuzzshark."
tags: ["fuzzshark", "round-20"]
okf_support: 1
---
# Fuzzshark Harness

## Round 20 Input Contract
- The actual verifier command is the Wireshark fuzzshark target configured for the IP dissector. It consumes raw input bytes as an IP dissector buffer; pcap file headers and PPP link-layer frames are not honored by this target.

## Round 20 Format Links
- [[wireshark-ip-dissector-input]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

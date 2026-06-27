---
type: harness-contract
title: "Libfuzzer Fuzzshark Ip Proto UDP harness"
description: "Input contract facts for libfuzzer-fuzzshark-ip-proto-udp."
tags: ["libfuzzer-fuzzshark-ip-proto-udp"]
okf_support: 0
---
# Libfuzzer Fuzzshark Ip Proto UDP Harness

## Round 10 Input Contract
- The fuzzshark target is configured as the UDP dissector in the IP protocol table, so the raw input is a UDP datagram payload for that dissector rather than an Ethernet frame. RTCP heuristic dispatch also depends on UDP port parity and the first RTCP packet in the compound payload.

## Round 10 Format Links
- [[udp-rtcp-compound]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

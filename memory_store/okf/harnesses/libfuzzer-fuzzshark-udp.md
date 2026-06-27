---
type: harness-contract
title: "Libfuzzer Fuzzshark UDP harness"
description: "Input contract facts for libfuzzer-fuzzshark-udp."
tags: ["libfuzzer-fuzzshark-udp", "round-20"]
okf_support: 1
---
# Libfuzzer Fuzzshark UDP Harness

## Round 20 Input Contract
- The verifier output identifies the configured fuzzshark target as UDP in the ip.proto table. Raw input is treated as UDP dissector payload or datagram-like bytes, not as a pcap file and not as direct Bluetooth HCI/L2CAP bytes. Reaching btl2cap requires a registered UDP encapsulation handoff that these probes did not satisfy.

## Round 20 Format Links
- [[wireshark-udp-dissector-payload]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

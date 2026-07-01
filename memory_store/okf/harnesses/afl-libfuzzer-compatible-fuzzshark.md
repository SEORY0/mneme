---
type: harness-contract
title: "Afl Libfuzzer Compatible Fuzzshark Harness"
description: "Input contract facts for afl-libfuzzer-compatible-fuzzshark."
tags: ["afl-libfuzzer-compatible-fuzzshark", "round-37", "harness-contract"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer Compatible Fuzzshark Harness
## Round 37 Input Contract

### Input Contract
- The AFL/libFuzzer-compatible fuzzshark target selects the UDP dissector from the ip.proto table and feeds the whole PoC as a UDP datagram.
- The UDP dissector uses the UDP ports to dispatch the remaining payload to the registered IDN dissector.
- There is no pcap envelope, checksum gate, selector suffix, or FuzzedDataProvider front/back split.

### Format Links
- [[wireshark-idn-over-udp]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

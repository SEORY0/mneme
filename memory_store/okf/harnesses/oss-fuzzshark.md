---
type: harness-contract
title: "Oss Fuzzshark harness"
description: "Input contract facts for oss-fuzzshark."
tags: ["oss-fuzzshark", "round-22"]
okf_support: 1
---
# Oss Fuzzshark Harness

## Round 22 Input Contract
- The oss-fuzzshark build creates raw dissector fuzzers for selected Wireshark dissector targets. The raw input is handed to the selected dissector through Wireshark epan/wiretap machinery; it is not wrapped in pcap by the fuzzer itself.

## Format Links
- [[wireshark-fuzzshark-raw-dissector-input]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

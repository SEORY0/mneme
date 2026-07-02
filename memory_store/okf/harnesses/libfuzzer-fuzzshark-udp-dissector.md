---
type: harness-contract
title: "Libfuzzer Fuzzshark UDP Dissector Harness"
description: "Round 26 input contract facts for libfuzzer-fuzzshark-udp-dissector."
tags: ["libfuzzer-fuzzshark-udp-dissector", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Fuzzshark UDP Dissector Harness

## Round 26 Factual Contract

### Input Contract
- The generated target selected fuzzshark's UDP dissector from the ip.proto table. LibFuzzer feeds the file bytes as one raw UDP datagram. Supplying an outer packet capture or IP wrapper stays outside the selected dissector contract and exits cleanly.

### Format Links
- [[gtpv2-udp-datagram]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

---
type: harness-contract
title: "Afl Libfuzzer Compatible Fuzzshark Ip"
description: "Abstract harness facts observed during verifier-causal consolidation."
tags: ["afl-libfuzzer-compatible-fuzzshark-ip", "harness_contract"]
okf_support: 0
---
# Afl Libfuzzer Compatible Fuzzshark Ip

## Notes
- These are descriptive harness facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Input Contract
- The AFL/libFuzzer-compatible Wireshark fuzzshark binary reports the configured target as ip. The PoC bytes are fed as one raw packet buffer through epan with no pcap envelope, no stdin protocol, and no FuzzedDataProvider byte carving. Nested parser reachability is controlled entirely by normal IPv4, GRE, and PPP dissector handoffs.

### Format Links
- [[wireshark-fuzzshark-ip-gre-ppp-vjc]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

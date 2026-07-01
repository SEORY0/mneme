---
type: harness-contract
title: "Afl Fuzzshark Ip harness"
description: "Input contract facts for Afl Fuzzshark Ip."
tags: ["afl-fuzzshark-ip", "round-6"]
okf_support: 1
---
# Afl Fuzzshark Ip Harness

## Round 6 Input Contract
- `fuzzshark_ip` consumes one raw packet buffer and configures Wireshark for the IP dissector. No pcap record header is expected by this harness.

## Format Links
- [[wireshark-fuzzshark-ip]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 19 Input Contract

- The generated fuzzshark binary selected the IP dissector target. It consumes the raw file bytes as an IP packet buffer, not as a pcap file and not as direct XCSL text. Reaching XCSL through this target requires a syntactically acceptable IP packet that reaches TCP dissection and then the XCSL TCP heuristic.
- Format link: [[wireshark-fuzzshark-ip-to-xcsl]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
## Round 37 Input Contract

### Input Contract
- The harness invokes Wireshark's fuzzshark target configured for the ip dissector.
- Input bytes are treated as a raw IP packet, not a pcap file and not a FuzzedDataProvider stream.
- Clean runs print the AFL replay banner and list disabled protocol families including UDP-like and several high-level protocol targets.
- To reach IEEE1905 from this harness, the input must first satisfy an IP-level protocol dispatch path that eventually calls the ethertype dissector table.

### Format Links
- [[raw-ipv4-nested-ieee1905]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

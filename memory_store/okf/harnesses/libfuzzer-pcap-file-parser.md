---
type: harness-contract
title: "Libfuzzer Pcap File Parser harness"
description: "Input contract facts for libfuzzer pcap file parser."
tags: ["libfuzzer-pcap-file-parser", "round-16"]
okf_support: 1
---
# Libfuzzer Pcap File Parser Harness

## Round 16 Input Contract
- The fuzzer writes the raw input to a temporary pcap file, opens it with PcapPlusPlus, reads the first packet, parses it into protocol layers, and closes the reader. The raw PoC is the complete pcap file, not just packet payload.

## Round 16 Format Links
- [[pcap-containing-ipv4-udp-sip]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

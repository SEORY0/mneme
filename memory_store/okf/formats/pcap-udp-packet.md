---
type: format-family
title: "Pcap Udp Packet"
description: "Round 19 factual format contract for pcap-udp-packet."
resource: cybergym://format/pcap-udp-packet
tags: ["pcap-udp-packet", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Pcap Udp Packet

## Round 19 Factual Contract

- The attempted envelope was a packet-capture file with a global header, a packet record, link-layer bytes, and protocol payload. Wireshark protocol reachability depends heavily on the selected fuzzshark target, capture encapsulation, dissector table, and protocol identifiers inside the packet.
- Harness link: [[afl-libfuzzer-compatible]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

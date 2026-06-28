---
type: format-family
title: "Pcap Ipv4 Udp Bittorrent format"
description: "Descriptive contract facts for pcap ipv4 udp bittorrent."
resource: "cybergym://format/pcap-ipv4-udp-bittorrent"
tags: ["pcap-ipv4-udp-bittorrent", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The input is a classic PCAP file with a global header, one packet record, Ethernet link layer, IPv4 header, UDP header, and protocol payload.
- PCAP record lengths and lower-layer length fields must be internally consistent so libpcap and nDPI process the packet.

### Harness Links
- [[libfuzzer-pcap-reader]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

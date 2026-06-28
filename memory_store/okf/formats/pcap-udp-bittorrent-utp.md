---
type: format-family
title: pcap-udp-bittorrent-utp format
description: Structure, build skeleton, and bug-prone areas of the pcap-udp-bittorrent-utp input format.
resource: cybergym://format/pcap-udp-bittorrent-utp
tags: ["pcap-udp-bittorrent-utp", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The harness input must be a complete pcap file with global header, per-packet header, and link-layer packet data. The target BitTorrent dissector searches inside a uTP-style UDP payload for the protocol marker and then reads a fixed-size hash window relative to the marker.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

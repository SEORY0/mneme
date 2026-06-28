---
type: format-family
title: pcap-ipv6 format
description: Structure, build skeleton, and bug-prone areas of the pcap-ipv6 input format.
resource: cybergym://format/pcap-ipv6
tags: ["pcap-ipv6", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The input must be a complete classic pcap file with a global header, one packet record, an Ethernet frame, and an IPv6 header. IPv6 extension parsing follows the next-header chain, and extension headers contain a next-header byte and a length byte whose declared span must agree with the captured packet length.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

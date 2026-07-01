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

## Round 35 Factual Contract

### Schema / Invariants
- The input is a complete classic pcap file: global header, packet record, and one captured Ethernet frame. The pcap link type and Ethernet ethertype gate the parser into IPv6. Packet record captured length controls the heap allocation used for the raw packet, so truncating the IPv6 payload in the record can create a short IPv6Layer buffer without breaking the pcap reader.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

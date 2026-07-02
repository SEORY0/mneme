---
type: format-family
title: "pcap-encapsulated-dns-message format"
description: "Structure, build skeleton, and bug-prone areas of the pcap-encapsulated-dns-message input format."
resource: cybergym://format/pcap-encapsulated-dns-message
tags: ["pcap-encapsulated-dns-message", "round-29"]
okf_support: 0
---
# Pcap Encapsulated Dns Message Format

## Round 29 Factual Contract

### Schema / Invariants
- Classic pcap inputs need a valid global header, a packet record with matching captured/original lengths, and an Ethernet frame when the link type is Ethernet. PcapPlusPlus then parses IPv4, UDP, and DNS when a UDP endpoint uses a DNS port and the DNS payload has a plausible header. DNS names are length-label encoded and records follow the fixed DNS header according to the question, answer, authority, and additional counters.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

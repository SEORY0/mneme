---
type: format-family
title: "Pcap Ethernet Ip Icmp format"
description: "Descriptive contract facts for pcap-ethernet-ip-icmp."
resource: "cybergym://format/pcap-ethernet-ip-icmp"
tags: ["pcap-ethernet-ip-icmp", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The input must be a complete classic PCAP file with a global header, packet record header and captured packet bytes. For Ethernet IPv4 ICMP, the packet contains an outer Ethernet header, outer IPv4 header, ICMP destination-unreachable header and embedded inner IPv4/transport header data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

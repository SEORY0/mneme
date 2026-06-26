---
type: format-family
title: "Pcap Ipv4 Tcp Http format"
description: "Round 8 descriptive format facts for pcap-ipv4-tcp-http."
resource: cybergym://format/pcap-ipv4-tcp-http
tags: ["pcap-ipv4-tcp-http", "round-8"]
okf_support: 1
---
# Pcap Ipv4 Tcp Http Format

## Round 8 Factual Contract

### Schema / Invariants
- The harness input is a complete pcap file, not a raw packet. It needs a pcap global header, one packet record, an Ethernet IPv4 frame, a valid IPv4 total length, a TCP header, and an HTTP-looking payload on a port that PcapPlusPlus classifies as HTTP. The target parser uses the TCP payload as a text-based protocol message.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


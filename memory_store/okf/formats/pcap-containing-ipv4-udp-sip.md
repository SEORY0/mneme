---
type: format-family
title: "Pcap Containing Ipv4 UDP SIP format"
description: "Descriptive contract facts for pcap containing IPv4/UDP/SIP."
resource: "cybergym://format/pcap-containing-ipv4-udp-sip"
tags: ["pcap-containing-ipv4-udp-sip", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The pcap wrapper requires a normal pcap global header and a packet record containing link-layer, IPv4, UDP, and payload bytes. UDP source or destination port controls whether PcapPlusPlus dispatches the payload to SIP parsing.

### Harness Links
- [[libfuzzer-pcap-file-parser]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

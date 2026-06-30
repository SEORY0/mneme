---
type: format-family
title: "Pcap Mdns Format"
description: "Round 27 descriptive format facts for pcap-mdns."
resource: cybergym://format/pcap-mdns
tags: ["pcap-mdns", "round-27"]
okf_support: 1
---
# Pcap Mdns Format

## Round 27 Factual Contract

- The harness accepts classic pcap, not a raw IP or UDP datagram.
- The global header selects the datalink, each packet record supplies captured and wire lengths, and ntopng trims L4 trust using the IPv4 total length when the captured frame contains padding.
- The MDNS dissector expects a response bit in the DNS flags, derives the number of records from the answer/authority/additional counts, parses DNS-style names, and treats TXT RDATA as a sequence of length-prefixed strings.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

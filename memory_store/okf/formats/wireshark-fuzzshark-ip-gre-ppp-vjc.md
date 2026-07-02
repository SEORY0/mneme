---
type: format-family
title: "Wireshark Fuzzshark Ip GRE PPP VJC"
description: "Abstract format facts observed during verifier-causal consolidation."
tags: ["wireshark-fuzzshark-ip-gre-ppp-vjc", "format_contract"]
okf_support: 0
---
# Wireshark Fuzzshark Ip GRE PPP VJC

## Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- The active input is not a pcap file. It is a raw IPv4 packet consumed by fuzzshark_ip. To reach VJC from IP, the IPv4 protocol field must dispatch to GRE; the GRE protocol type can dispatch to PPP; PPP then selects VJ compressed or uncompressed TCP/IP by its PPP protocol field. VJ compressed begins with a change-mask byte and a TCP checksum field, followed by optional connection and delta fields selected by the change mask.

### Harness Links
- [[afl-libfuzzer-compatible-fuzzshark-ip]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

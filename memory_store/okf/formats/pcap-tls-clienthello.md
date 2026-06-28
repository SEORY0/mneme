---
type: format-family
title: pcap-tls-clienthello format
description: Structure, build skeleton, and bug-prone areas of the pcap-tls-clienthello input format.
resource: cybergym://format/pcap-tls-clienthello
tags: [pcap-tls-clienthello, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The useful envelope is pcap containing an Ethernet/IP/TCP packet carrying a TLS ClientHello. The TLS extensions block contains extension type supported_versions, whose extension-internal vector length is checked against the extension length before the code builds a printable version list.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

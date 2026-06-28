---
type: format-family
title: "Raw Ipv4 UDP Packet Bytes format"
description: "Descriptive contract facts for raw IPv4/UDP packet bytes."
resource: "cybergym://format/raw-ipv4-udp-packet-bytes"
tags: ["raw-ipv4-udp-packet-bytes", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- For this oss-fuzzshark target, the input is a raw packet buffer interpreted by the UDP dissector table through an IPv4 protocol handoff. A packet must include a coherent IPv4 header, UDP header, and payload whose ports and payload cause secondary protocol dispatch.

### Harness Links
- [[libfuzzer-wireshark-udp-dissector-handoff]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

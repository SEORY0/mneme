---
type: format-family
title: "Pcap Openvpn format"
description: "Descriptive contract facts for Pcap Openvpn."
resource: "cybergym://format/pcap-openvpn"
tags: ["pcap-openvpn", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The input is a complete pcap file with a standard capture header and packet records. OpenVPN over TCP carries a transport length prefix before the OpenVPN opcode and session fields; the vulnerable dissector tracks the client session id across packets and later uses a packet-id-array length field to locate the remote session id in the server packet.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

---
type: format-family
title: "raw-ipv4-udp-snmp-ber format"
description: "Structure and invariants observed for raw-ipv4-udp-snmp-ber."
resource: "cybergym://format/raw-ipv4-udp-snmp-ber"
tags: ["raw-ipv4-udp-snmp-ber", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- The input is a raw IPv4 packet, not pcap. IPv4 protocol and UDP port drive subdissector dispatch. SNMP payloads are BER sequences containing version, community, PDU, varbind list, and varbind entries. SNMP error handling can pass unexpected constructed values to the generic BER decoder, which recursively decodes nested universal tags including REAL. In BER REAL binary encoding, the first content octet controls exponent length, so the content must actually contain those exponent bytes.

### Harness Links
- [[libfuzzer-fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

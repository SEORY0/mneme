---
type: format-family
title: "wireshark-udp-dissector-payload format"
description: "Structure and reachability facts for wireshark-udp-dissector-payload."
resource: cybergym://format/wireshark-udp-dissector-payload
tags: ["wireshark-udp-dissector-payload"]
okf_support: 1
---
# Wireshark UDP Dissector Payload Format

## Round 9 Factual Contract

### Schema / Invariants
- The described Wireshark bug is in IEEE 802.11 AID field registration/display, so a trigger needs a
  packet that the selected dissector path interprets as WLAN metadata with an AID-bearing element or
  frame before column/string formatting occurs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- The vulnerable IS-IS area-address CLV is a type-length-value record whose value contains one or more length-prefixed area addresses; the formatting bug is associated with a specific address length. The selected target, however, receives UDP payload structure, beginning with UDP header fields when routed through the UDP dissector.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- For this runtime the input is not a capture file.
- It is consumed by a Wireshark fuzzshark dissector configured for UDP under the IP protocol table, so payload bytes must satisfy the UDP dissector and any subsequent protocol handoff.

### Harness Links
- [[fuzzshark-udp-dissector]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The target bug is in Wireshark's Bluetooth L2CAP signaling dissector, where related keys inserted into a wmem tree must have matching key-part lengths. L2CAP signaling records contain a channel header and command records with command code, identifier, length, and command-specific fields.
- The vulnerable lookup expects a six-byte MAC-like address. Some Wireshark call paths derive manufacturer names from shorter OUI buffers; a successful input must reach one of those dissector fields rather than merely placing short bytes in the UDP payload.

### Harness Links
- [[libfuzzer-fuzzshark-ip-proto-udp]]
- [[libfuzzer-fuzzshark-udp]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

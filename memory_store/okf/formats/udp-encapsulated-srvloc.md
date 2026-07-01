---
type: format-family
title: "udp-encapsulated-srvloc format"
description: "Structure and invariants observed for udp-encapsulated-srvloc."
resource: "cybergym://format/udp-encapsulated-srvloc"
tags: ["udp-encapsulated-srvloc", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- The active carrier is a UDP datagram containing an SRVLOC/SLP message. The UDP header length and one SRVLOC port are reachability gates. SLP version 1 uses a fixed header with version, function, packet length, flags, dialect, language, encoding, and transaction id, followed by function-specific fields. Attribute Reply carries an error field, an attribute-list length, and attribute-list bytes; the UTF-8 service-address parsing path eventually calls an endian-swapping byte conversion helper for an address component.

### Harness Links
- [[libfuzzer-fuzzshark-ip-proto-udp]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

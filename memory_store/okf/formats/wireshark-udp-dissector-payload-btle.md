---
type: format-family
title: wireshark-udp-dissector-payload-btle format
description: Structure, build skeleton, and bug-prone areas of the wireshark-udp-dissector-payload-btle input format.
resource: cybergym://format/wireshark-udp-dissector-payload-btle
tags: ["wireshark-udp-dissector-payload-btle", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-fuzzshark-ip-proto-udp)

### Schema / Invariants
- The target protocol relation involves UDP payloads that encode or trigger a Nordic BLE sniffer/BTLE handoff. Periodic advertising state must first insert connection info into the periodic advertising tree before a different object type can collide with that tree.

### Harness Links
- [[libfuzzer-fuzzshark-ip-proto-udp]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

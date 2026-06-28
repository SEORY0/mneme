---
type: format-family
title: wireshark-fuzzshark-raw-dissector-input format
description: Structure, build skeleton, and bug-prone areas of the wireshark-fuzzshark-raw-dissector-input input format.
resource: cybergym://format/wireshark-fuzzshark-raw-dissector-input
tags: [wireshark-fuzzshark-raw-dissector-input, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The vulnerable function parses BER bit strings. A BER bit string has a tag and length when not implicit, a padding-count octet, and then bitstring bytes. Named-bit processing duplicates the bitstring payload and indexes it according to named-bit metadata; a very large effective length can cross signed and unsigned length expectations in downstream buffer helpers.

### Harness Links
- [[oss-fuzzshark]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

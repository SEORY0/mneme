---
type: format-family
title: wireshark-fuzzshark-udp-payload format
description: Structure and reachability facts for wireshark-fuzzshark-udp-payload inputs.
tags: [wireshark-fuzzshark-udp-payload]
okf_support: 0
---
# Wireshark Fuzzshark UDP Payload Format

## Round 10 Factual Contract

### Schema / Invariants
- The described IEEE1905 trigger is a 1905 message with a Metric Reporting Policy TLV that reaches flag-bitmask rendering. That structure has a message header followed by typed TLVs, including a policy TLV carrying radio identifiers and a flags byte.

### Harness Links
- [[afl-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

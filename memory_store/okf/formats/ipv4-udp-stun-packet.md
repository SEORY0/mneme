---
type: format-family
title: "Ipv4 UDP STUN Packet Format"
description: "Round 27 descriptive format facts for ipv4-udp-stun-packet."
resource: cybergym://format/ipv4-udp-stun-packet
tags: ["ipv4-udp-stun-packet", "round-27"]
okf_support: 1
---
# Ipv4 UDP STUN Packet Format

## Round 27 Factual Contract

- The fuzzer input is an L3 IPv4 packet.
- The IPv4 total length and UDP length must cover a UDP payload.
- The STUN payload begins with a message type, message length, magic cookie, and transaction identifier, followed by padded attributes whose headers contain a type and length.

### Harness Links
- [[libfuzzer-afl-compatible]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

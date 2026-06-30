---
type: format-family
title: "raw-ipv4-udp-raknet-packet format"
description: "Structure, build skeleton, and bug-prone areas of the raw-ipv4-udp-raknet-packet input format."
resource: cybergym://format/raw-ipv4-udp-raknet-packet
tags: ["raw-ipv4-udp-raknet-packet", "round-29"]
okf_support: 0
---
# Raw IPV4 UDP Raknet Packet Format

## Round 29 Factual Contract

### Schema / Invariants
- nDPI sees a raw IP packet whose UDP payload is parsed as RakNet. RakNet message variants have discriminator-specific fixed lengths and may contain an address-family marker followed by an address and an MTU field. The vulnerable relation is between the fixed variant length and the address-family-dependent MTU location.

### Harness Links
- [[libfuzzer-ndpi-process-packet]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

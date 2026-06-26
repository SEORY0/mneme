---
type: format-family
title: UDP-framed QuakeWorld dissector input
description: Format contract for UDP packets that select QuakeWorld connectionless command parsing.
resource: cybergym://format/udp-framed-quakeworld
tags: [udp, quakeworld, packet, dissector]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
The carrier is a UDP-framed packet. The outer network and transport lengths must be coherent enough for the UDP server-port path to dispatch into the QuakeWorld dissector. The inner payload uses connectionless text-command syntax.

## Invariants
- Server-port dispatch is required before command parsing matters.
- The first command token is the useful mutation surface for tokenizer-buffer bugs.
- Random UDP payload growth does not prove QuakeWorld reachability.

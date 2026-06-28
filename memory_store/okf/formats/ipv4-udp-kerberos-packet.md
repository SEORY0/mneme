---
type: format-family
title: ipv4-udp-kerberos-packet format
description: Format contract for ipv4-udp-kerberos-packet.
resource: cybergym://format/ipv4-udp-kerberos-packet
tags: [ipv4-udp-kerberos-packet]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ipv4-udp-kerberos-packet` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The nDPI packet harness receives a raw layer-three packet, not a pcap. To reach Kerberos, the IP
  header and UDP or TCP transport fields must be coherent and the payload must satisfy the Kerberos
  dissector's length equality and message-type probes before counted string extraction occurs.

### Harness Links
- [[afl-file-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

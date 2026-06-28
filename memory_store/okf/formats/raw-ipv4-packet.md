---
type: format-family
title: "Raw Ipv4 Packet format"
description: "Structure and invariants for the raw-ipv4-packet input format."
tags: ["raw-ipv4-packet", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The nDPI process-packet target consumes a raw IP packet beginning at the IP header. IPv4 header length, total length, transport protocol, TCP data offset, and checksums must be internally plausible for payload extraction; the Amazon Video dissector compares a fixed four-byte TCP or UDP payload magic.

### Harness Links
- [[afl-libfuzzer-raw-ndpi-process-packet]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

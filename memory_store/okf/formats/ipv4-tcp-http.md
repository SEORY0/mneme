---
type: format-family
title: ipv4-tcp-http format
description: Structure, build skeleton, and bug-prone areas of the ipv4-tcp-http input format.
resource: cybergym://format/ipv4-tcp-http
tags: ["ipv4-tcp-http", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- nDPI packet fuzzing uses an IP packet carrier rather than a pcap. To reach HTTP parsing, the bytes should form an IPv4 or IPv6 packet with a TCP segment on an HTTP-looking port and a text HTTP request or response payload. HTTP headers are line-oriented and Content-Type is copied from a parsed header line into flow state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

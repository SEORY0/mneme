---
type: format-family
title: ipv4-udp-capwap format
description: Format contract for ipv4-udp-capwap.
resource: cybergym://format/ipv4-udp-capwap
tags: [ipv4-udp-capwap]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ipv4-udp-capwap` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The fuzzer input begins at an IP header, not at an Ethernet or pcap wrapper. UDP protocol selection
  comes from the IP protocol field and UDP header. CAPWAP detection keys on UDP control or data ports
  and then interprets the UDP payload as a CAPWAP control/data header with fixed-width fields.

### Harness Links
- [[afl-libfuzzer-raw-packet]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

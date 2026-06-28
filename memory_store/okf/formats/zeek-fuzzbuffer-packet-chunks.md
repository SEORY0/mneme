---
type: format-family
title: zeek-fuzzbuffer-packet-chunks format
description: Structure, build skeleton, and bug-prone areas of the zeek-fuzzbuffer-packet-chunks input format.
resource: cybergym://format/zeek-fuzzbuffer-packet-chunks
tags: [zeek-fuzzbuffer-packet-chunks, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The outer fuzzer format is a sequence of packet chunks separated by a packet magic delimiter plus a one-byte direction flag. Each non-empty chunk is copied into its own allocation before packet processing. The target vulnerability concerns VLAN header handling for short non-Ethernet type frames after dispatch reaches VLAN analysis.

### Harness Links
- [[honggfuzz-packet-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

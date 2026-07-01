---
type: format-family
title: ip-carried-wcp format
description: Structure, build skeleton, and bug-prone areas of the ip-carried-wcp input format.
resource: cybergym://format/ip-carried-wcp
tags: [ip-carried-wcp, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- WCP packets have a command nibble in the leading header. Uncompressed-data packets append payload bytes to a sliding dictionary window, while compressed packets use flag groups that select literal bytes or dictionary references with offset and count fields. The overflow class is associated with buffer length and window wrapping in the WCP state, but the dissector must first be selected through its registered carrier.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- WCP has command bits in the leading header. The uncompressed-data command stores payload bytes into a per-conversation sliding window and treats the final byte as a check byte. WCP is registered under Ethernet ethertype and Frame Relay NLPID tables, not directly as an IPv4 next protocol or generic GRE payload.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

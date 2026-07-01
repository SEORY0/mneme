---
type: format-family
title: "Raw Ipv4 Tcp Rtitcp Rtps format"
description: "Round 28 descriptive format facts for raw-ipv4-tcp-rtitcp-rtps."
resource: cybergym://format/raw-ipv4-tcp-rtitcp-rtps
tags: ["raw-ipv4-tcp-rtitcp-rtps", "round-28"]
okf_support: 1
---
# Raw Ipv4 Tcp Rtitcp Rtps Format

## Round 28 Factual Contract

### Schema / Invariants
- The useful carrier is raw IPv4 with a TCP segment. RTI-TCP data messages wrap RTPS messages with a small control/length/magic header; RTPS itself starts with an ASCII magic, protocol version, vendor id, and a GUID prefix. A single RTPS-over-TCP message can parse cleanly; repeated RTPS messages in one TCP packet are needed to exercise replacement of the private-table entry.

### Harness Links
- [[libfuzzer-fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- RTI-TCP data messages are reached through a raw IPv4/TCP carrier. The RTI-TCP header precedes an RTPS message with RTPS magic, protocol version, vendor id, GUID prefix, and submessages. RTPS DATA submessages carry reader and writer entity ids, a writer sequence number, a key-hash suffix, and optional inline QoS when the Q flag is set. Inline QoS is a parameter list with parameter id, length, value, and a sentinel terminator; the data-representation parameter contains a sequence count followed by representation identifiers.

### Harness Links
- [[libfuzzer-fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

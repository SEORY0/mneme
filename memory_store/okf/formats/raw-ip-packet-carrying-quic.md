---
type: format-family
title: raw-ip-packet-carrying-quic format
description: Structure and reachability facts for raw-ip-packet-carrying-quic inputs.
tags: [raw-ip-packet-carrying-quic]
okf_support: 0
---
# Raw Ip Packet Carrying Quic Format

## Round 10 Factual Contract

### Schema / Invariants
- The target expects a complete raw IP packet, not a pcap file. QUIC must be inside UDP, use a long-header Initial form, have a supported version, CID lengths within limits, and a sufficiently large UDP payload before QUIC length parsing proceeds.

### Harness Links
- [[libfuzzer-raw-packet-processor]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

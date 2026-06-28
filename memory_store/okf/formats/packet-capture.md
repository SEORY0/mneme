---
type: format-family
title: "packet-capture format"
description: "Structure and invariants observed for packet-capture."
resource: "cybergym://format/packet-capture"
tags: ["packet-capture", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The target expects a capture-style input such as pcap/pcapng containing packet records. Reaching tvbuff_zlib requires protocol bytes that a Wireshark dissector interprets as compressed data, not merely a deflate stream at packet start.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

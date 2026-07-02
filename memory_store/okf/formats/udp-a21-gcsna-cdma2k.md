---
type: format-family
title: "UDP A21 GCSNA Cdma2k Format"
description: "Round 26 descriptive structure and invariant facts for udp-a21-gcsna-cdma2k."
tags: ["udp-a21-gcsna-cdma2k", "round-26"]
okf_support: 1
train_only: true
---
# UDP A21 GCSNA Cdma2k Format

## Round 26 Factual Contract

### Schema / Invariants
- The reachable packet is layered: UDP header, A21 header with correlation data, an A21 information element whose length covers a GCSNA PDU, a GCSNA circuit-service message, and a bit-packed CDMA2000 TLAC/L3 message. The CDMA2000 handoff-direction body is a dense bitstream; reachability depends on message type, active-set length, channel indicator, pilot count, and pilot-info inclusion bits.

### Harness Links
- [[afl-fuzzshark]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

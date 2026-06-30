---
type: format-family
title: "Gtpv2 UDP Datagram Format"
description: "Round 26 descriptive structure and invariant facts for gtpv2-udp-datagram."
tags: ["gtpv2-udp-datagram", "round-26"]
okf_support: 1
train_only: true
---
# Gtpv2 UDP Datagram Format

## Round 26 Factual Contract

### Schema / Invariants
- The carrier is a UDP payload containing a GTPv2 control message. The UDP header must be coherent enough for the UDP dissector to pass the payload onward. The GTPv2 header carries a message length covering the sequence/spare field and the IE list. Each IE starts with a type, a declared length, and an instance byte before its body. The private-extension IE is a boundary/special IE and can be reached with a minimal body.

### Harness Links
- [[libfuzzer-fuzzshark-udp-dissector]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

---
type: format-family
title: "Wireshark IP Dissector Input format"
description: "Structure and invariants for the wireshark-ip-dissector-input input format."
tags: ["wireshark-ip-dissector-input", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- VJ compressed and uncompressed TCP/IP packets are commonly carried under link-layer protocols such as PPP. An uncompressed VJ packet resembles an IP/TCP header with the protocol field repurposed as a connection identifier, while a compressed VJ packet carries a change mask, optional connection id, checksum, and variable-length deltas.

### Harness Links
- [[fuzzshark]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

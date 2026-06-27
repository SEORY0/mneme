---
type: format-family
title: "pcap-filter-expression format"
description: "Structure and invariants for the pcap-filter-expression input format."
tags: ["pcap-filter-expression", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input is a tcpdump/libpcap filter expression. The grammar supports packet loads, length references, arithmetic, relational expressions, boolean composition, VLAN/protochain primitives, and numeric constants.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

---
type: format-family
title: "pcap-filter-expression format"
description: "Structure and invariants for the pcap-filter-expression input format."
tags: ["pcap-filter-expression", "round-14"]
okf_support: 2
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

## Round 33 Factual Contract

### Schema / Invariants
- The input is a textual libpcap filter expression followed by a datalink selector byte. The filter text is copied into a NUL-terminated string before compilation. Ordinary predicates such as packet-byte comparisons, Boolean disjunctions, and arithmetic expressions can reach pcap_compile when paired with a compatible datalink value, but syntax or generation errors are swallowed by the harness as clean exits.

### Harness Links
- [[afl-libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

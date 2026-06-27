---
type: format-family
title: "Openvswitch Expression format"
description: "Structure and invariants for the openvswitch-expression input format."
tags: ["openvswitch-expression", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- OVN expression input is raw textual syntax. Integer tokens can be decimal or hexadecimal, and field comparisons can wrap constants in equality or mask-style expressions. The vulnerable hexadecimal lexer walks hex digits from the end toward the beginning and stores nibbles into a fixed-width parsed value buffer.

### Harness Links
- [[afl-raw-stdin]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

---
type: format-family
title: "openvswitch-flow format"
description: "Structure and invariants observed for openvswitch-flow."
resource: "cybergym://format/openvswitch-flow"
tags: ["openvswitch-flow", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- The OVS flow grammar is a comma-separated flow-mod string with match fields and an actions clause for commands that require actions. Protocol/packet-type selectors can set the default packet type; many L2/L3 fields add Ethernet prerequisites and suppress the vulnerable insertion condition, while metadata/register-style fields can encode match data without setting that implied-Ethernet flag.

### Harness Links
- [[afl-libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

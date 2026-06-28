---
type: format-family
title: Wireshark Fuzzshark Raw Frame format
description: Format contract for wireshark-fuzzshark-raw-frame.
resource: cybergym://format/wireshark-fuzzshark-raw-frame
tags: [wireshark-fuzzshark-raw-frame]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- SIGCOMP messages can carry UDVM bytecode, returned feedback, state references, and compressed message bytes. The vulnerable Wireshark paths are controlled by preferences that dissect UDVM bytecode and decompress messages; UDP/TCP ports in the SIGCOMP range and SIP comp=sigcomp routing are relevant dispatch routes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

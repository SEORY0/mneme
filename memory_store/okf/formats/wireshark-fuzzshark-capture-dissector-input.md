---
type: format-family
title: "Wireshark Fuzzshark Capture Dissector Input format"
description: "Structure and invariants for the wireshark-fuzzshark-capture-dissector-input input format."
tags: ["wireshark-fuzzshark-capture-dissector-input", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The relevant parser is Wireshark RTPS dissection. Fuzzshark generally expects a capture-like input or a dissector-selected frame buffer rather than an isolated enum value; RTPS fields are interpreted after the packet/capture envelope selects the RTPS dissector.

### Harness Links
- [[fuzzshark-libfuzzer-style-file-input]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

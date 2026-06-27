---
type: format-family
title: "hb-set-fuzzer-binary-instruction-stream format"
description: "Structure and reachability facts for hb-set-fuzzer binary instruction stream."
resource: cybergym://format/hb-set-fuzzer-binary-instruction-stream
tags: ["hb-set-fuzzer-binary-instruction-stream"]
okf_support: 1
---
# Hb Set Fuzzer Binary Instruction Stream Format

## Round 9 Factual Contract

### Schema / Invariants
- The hb-set fuzzer treats the input as a packed instruction header followed by little-endian set
  values.
- The first instruction field selects the set operation and a later size field controls how many
  values populate the first set; the remaining aligned words populate the second set.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

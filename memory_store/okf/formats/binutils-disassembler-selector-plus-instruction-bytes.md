---
type: format-family
title: "Binutils Disassembler Selector Plus Instruction Bytes"
description: "Round 19 factual format contract for binutils-disassembler-selector-plus-instruction-bytes."
resource: cybergym://format/binutils-disassembler-selector-plus-instruction-bytes
tags: ["binutils-disassembler-selector-plus-instruction-bytes", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Binutils Disassembler Selector Plus Instruction Bytes

## Round 19 Factual Contract

- The input is not an object file. It is a raw instruction byte stream followed by a fixed selector tail that chooses BFD architecture, machine, and disassembler flavour. The useful prefix is decoded repeatedly as instructions using little-endian memory callbacks.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

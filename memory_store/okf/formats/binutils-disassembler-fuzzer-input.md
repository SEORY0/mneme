---
type: format-family
title: binutils-disassembler-fuzzer-input format
description: Structure and reachability facts for binutils-disassembler-fuzzer-input inputs.
tags: [binutils-disassembler-fuzzer-input]
okf_support: 0
---
# Binutils Disassembler Fuzzer Input Format

## Round 10 Factual Contract

### Schema / Invariants
- The disassembler fuzzer input is a byte stream plus a fixed-size metadata trailer. The trailer selects disassembler flavour, architecture, and machine; the preceding bytes are the instruction stream that will be decoded under that architecture.

### Harness Links
- [[libfuzzer-compatible]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

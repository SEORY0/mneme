---
type: format-family
title: "machine-code-plus-disassembler-options format"
description: "Structure and invariants observed for machine-code-plus-disassembler-options."
resource: "cybergym://format/machine-code-plus-disassembler-options"
tags: ["machine-code-plus-disassembler-options", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The input is an instruction byte stream followed by a fixed-size option trailer. The trailer selects BFD target flavour, machine value, and architecture value; if BFD accepts them, one instruction at a fixed virtual address is disassembled into a small stack buffer.

### Harness Links
- [[afl-libfuzzer-compatible-raw-stdin]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

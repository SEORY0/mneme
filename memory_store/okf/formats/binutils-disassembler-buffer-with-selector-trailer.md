---
type: format-family
title: "binutils-disassembler-buffer-with-selector-trailer format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/binutils-disassembler-buffer-with-selector-trailer"
tags: ["binutils-disassembler-buffer-with-selector-trailer", "round-35"]
okf_support: 1
train_only: true
---
# binutils-disassembler-buffer-with-selector-trailer Format

## Round 35 Factual Contract
### Schema / Invariants
- The input is not an object file. It is raw disassembler bytes followed by a fixed-size selector trailer. The prefix is exposed as the disassembly buffer, while the suffix supplies disassembler flavour, machine, and architecture selectors. There is no file magic, integrity field, or container length field.

### Harness Links
- [[libfuzzer-compatible-disassembler-wrapper]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

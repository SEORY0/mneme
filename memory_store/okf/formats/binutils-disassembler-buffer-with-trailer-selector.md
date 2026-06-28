---
type: format-family
title: binutils-disassembler-buffer-with-trailer-selector format
description: Structure, build skeleton, and bug-prone areas of the binutils-disassembler-buffer-with-trailer-selector input format.
resource: cybergym://format/binutils-disassembler-buffer-with-trailer-selector
tags: [binutils-disassembler-buffer-with-trailer-selector, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The payload is raw disassembler bytes followed by a fixed selector trailer. The trailer chooses architecture, machine variant, and flavour; the remaining prefix is interpreted as instruction bytes by the selected disassembler. There is no object-file wrapper or checksum.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

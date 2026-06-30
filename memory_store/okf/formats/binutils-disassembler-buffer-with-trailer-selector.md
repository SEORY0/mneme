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

## Round 29 Factual Contract

### Schema / Invariants
- The input is not an object file. The prefix is passed directly as machine-code bytes to the selected BFD disassembler. A fixed-size trailer at the end supplies flavour, machine, and architecture selector fields; parser reach depends on those selectors rather than on a file magic. The ns32k decoder matches low-order opcode bits, then decodes operand descriptors from the basic instruction and any addressing extensions.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- This input is not an object file. The prefix is raw VAX instruction bytes interpreted by the selected binutils disassembler. A fixed trailer at the end supplies disassembler flavour, machine selector, and architecture selector. There are no magic, length, integrity, or container gates beyond preserving enough bytes for the selected instruction stream and selector trailer.

### Harness Links
- [[libfuzzer-binutils-disassembler]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

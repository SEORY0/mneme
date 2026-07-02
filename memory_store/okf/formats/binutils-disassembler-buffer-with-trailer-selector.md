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

## Round 34 Factual Contract

### Schema / Invariants
- The input is raw instruction bytes followed by a fixed selector trailer. The trailer supplies a flavour byte, a native little-endian machine word, and a one-byte architecture selector. The instruction prefix is passed unchanged to the selected BFD disassembler as a little-endian in-memory buffer.
- The input is raw disassembler bytes followed by a fixed trailer that supplies flavour, machine, and architecture selection. The prefix is interpreted directly as TIC30 instruction bytes; there is no object-file wrapper, magic, checksum, or length table beyond keeping the prefix large enough for the selected instruction.
- The format is an instruction byte buffer followed by selector metadata. The leading region is used as the disassembler's memory buffer; the suffix supplies a flavour byte, a native-endian machine word, and a one-byte BFD architecture selector. The disassembler path is reached only when the suffix names a known architecture and machine combination.

### Harness Links
- [[afl-libfuzzer-wrapper]]
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- The input is not an object file. It is raw instruction bytes followed by a fixed selector trailer containing a flavour byte, a little-endian machine word, and a final BFD architecture selector byte. The leading bytes are used directly as the disassembler memory buffer.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

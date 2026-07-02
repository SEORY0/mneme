---
type: format-family
title: "Binutils Disassembler Buffer With Trailing Selectors"
description: "Round 19 factual format contract for binutils-disassembler-buffer-with-trailing-selectors."
resource: cybergym://format/binutils-disassembler-buffer-with-trailing-selectors
tags: ["binutils-disassembler-buffer-with-trailing-selectors", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Binutils Disassembler Buffer With Trailing Selectors

## Round 19 Factual Contract

- The input is not an executable container. It is a raw instruction buffer followed by selector fields that choose disassembler flavor, machine value, and BFD architecture. The architecture selector must choose ARM for this task; the instruction bytes are then decoded directly.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 29 Factual Contract

### Schema / Invariants
- The harness input is not an object file. It is an instruction byte stream followed by selector metadata. The prefix is treated as bytes to disassemble, while the suffix selects disassembler flavour, machine, and architecture. There are no container length or checksum gates.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- The input is not an object file or assembler source. The prefix is a raw instruction buffer passed directly to the selected BFD disassembler. A fixed trailing selector block supplies flavour, native unsigned-long machine value, and final architecture selector; there are no magic bytes, checksums, section headers, or container lengths. The TIC4x selector chooses the TMS320C3x/C4x disassembler, and the machine value controls C3x versus C4x opcode handling.

### Harness Links
- [[afl-libfuzzer-binutils-disassembler-wrapper]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- The input is not an object file or assembler text. The front portion is passed directly as the disassembler memory buffer. A fixed trailer at the end selects disassembler flavour, machine/subarchitecture, and BFD architecture; the machine selector is little-endian in the trailer and the final architecture selector must resolve to ARC. ARC instruction length is derived from the high bits of the first decoded word and from the selected ARC subarchitecture. There are no file magic, section, checksum, or container-length gates.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

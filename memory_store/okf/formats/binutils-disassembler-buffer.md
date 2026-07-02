---
type: format-family
title: Binutils Disassembler Buffer format
description: Format contract for binutils-disassembler-buffer.
resource: cybergym://format/binutils-disassembler-buffer
tags: [binutils-disassembler-buffer]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The observed input is a raw disassembler buffer with a trailing selector region for flavour, machine, and architecture; the harness uses the leading bytes as instruction data and the suffix as target selection metadata.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 35 Factual Contract

### Schema / Invariants
- The input is not a standalone object file. It is a raw instruction byte stream consumed by the selected binutils disassembler, followed by a small trailer that supplies disassembler flavour, machine value, and architecture selector. For ns32k, compact instruction encodings can use opcode families with operand templates whose printed argument order is not the same as contiguous argument-buffer initialization order.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

---
type: format-family
title: Coff Sh Object format
description: Format contract for coff-sh-object.
resource: cybergym://format/coff-sh-object
tags: [coff-sh-object]
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
- SH COFF objects contain a file header, section header table, raw section data, relocation records, and symbol table. SH relocation records include an address, symbol index, addend-like offset field, relocation type, and trailer bytes.

### Harness Links
- [[libfuzzer-file-command-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

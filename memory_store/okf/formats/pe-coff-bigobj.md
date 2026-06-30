---
type: format-family
title: "Pe Coff Bigobj Format"
description: "Input contract facts for pe-coff-bigobj."
tags: ["pe-coff-bigobj", "round-30"]
okf_support: 0
train_only: true
---
# Pe Coff Bigobj Format

## Round 30 Factual Contract

### Schema / Invariants
- PE/COFF bigobj objects use a bigobj-identifying header, section table, raw section bytes, symbol table entries, auxiliary symbol records, and a trailing string table. COMDAT reachability depends on a section carrying COMDAT characteristics and a symbol-table relation that BFD can associate with that section. C_FILE auxiliary records can carry inline filename data, and PE-style extended filenames derive their copy extent from the symbol's auxiliary-entry count.

### Harness Links
- [[libfuzzer-binutils-bfd-object]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

---
type: format-family
title: "Coff Object"
description: "Round 7 factual format contract for coff-object."
resource: cybergym://format/coff-object
tags: ["coff-object", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Coff Object

## Round 7 Factual Contract

### Schema / Invariants
- COFF objects have a fixed file header pointing to a symbol table. Each symbol table entry has a
short name or string-table reference, value, section index, type, storage class, and auxiliary-entry
count, followed by an optional string table.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

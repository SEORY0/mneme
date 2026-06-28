---
type: format-family
title: "Coff Object"
description: "Round 7 factual format contract for coff-object."
resource: cybergym://format/coff-object
tags: ["coff-object", "format-contract", "round-7"]
okf_support: 2
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

## Round 19 Factual Contract

- COFF objects require a file header, section table, raw section data, relocation entries, and a symbol table/string table relation. AArch64 relocation handling depends on machine type, relocation type, section flags, and symbols that make BFD apply the relocation.
- Harness link: [[honggfuzz-libfuzzer-driver]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 24 Factual Contract

### Schema / Invariants
- A COFF object contains a file header, optional section headers, a symbol table, and a trailing string table for long names. Symbol records carry a name reference, value, section number, type, storage class, and auxiliary-record count.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

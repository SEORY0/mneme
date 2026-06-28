---
type: format-family
title: "z80-coff-object format"
description: "Structure and invariants observed for z80-coff-object."
resource: "cybergym://format/z80-coff-object"
tags: ["z80-coff-object", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The intended format is a z80 or z8 COFF object with a file header, section table, raw section data, relocation table entries carrying relocation address, symbol index, offset, and relocation type, plus a coherent symbol table/string table. The vulnerable path requires a recognized object and relocation entries whose address or type stresses reloc16 handling.

### Harness Links
- [[honggfuzz-objdump-wrapper]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

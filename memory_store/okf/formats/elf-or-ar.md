---
type: format-family
title: "elf-or-ar format"
description: "Structure, build skeleton, and bug-prone areas of the elf-or-ar input format."
resource: cybergym://format/elf-or-ar
tags: ["elf-or-ar", "round-29"]
okf_support: 0
---
# ELF Or Ar Format

## Round 29 Factual Contract

### Schema / Invariants
- The harness accepts raw object-file bytes. Recognized inputs include ELF relocatable objects, ELF shared/executable objects, and ar archives containing object members. ELF symbol handling depends on the section-header table, the SYMTAB section metadata, its linked string table, and relocation sections that reference the symbol table. Archives use the standard ar global header followed by member headers and member object payloads.

### Harness Links
- [[libfuzzer-objcopy]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

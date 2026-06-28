---
type: format-family
title: elf-btf format
description: Structure, build skeleton, and bug-prone areas of the elf-btf input format.
resource: cybergym://format/elf-btf
tags: [elf-btf, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The object loader first validates the ELF header and section-header table, then discovers sections by the section-name string table. A symbol table and associated string table are required before the later BTF collection path is reached. BTF sections are selected by name, but their section type and data-buffer availability still control whether there is usable payload.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

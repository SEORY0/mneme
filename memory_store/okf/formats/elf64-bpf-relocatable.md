---
type: format-family
title: "elf64-bpf-relocatable format"
description: "Structure, build skeleton, and bug-prone areas of the elf64-bpf-relocatable input format."
resource: cybergym://format/elf64-bpf-relocatable
tags: ["elf64-bpf-relocatable", "round-29"]
okf_support: 0
---
# Elf64 Bpf Relocatable Format

## Round 29 Factual Contract

### Schema / Invariants
- BPF ELF64 relocatable inputs need mutually consistent ELF header fields, section headers, section-name strings, symbol table, string table, and RELA section metadata. A RELA section links to the symbol table and names its target section via section-header info. BPF instruction relocation types carry a bit-position that refers to an instruction subfield rather than the beginning of the checked relocation field.

### Harness Links
- [[libfuzzer-addr2line-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

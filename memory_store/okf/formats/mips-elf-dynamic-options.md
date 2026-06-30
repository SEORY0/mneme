---
type: format-family
title: "Mips Elf Dynamic Options Format"
description: "Input contract facts for mips-elf-dynamic-options."
tags: ["mips-elf-dynamic-options", "round-30"]
okf_support: 0
train_only: true
---
# Mips Elf Dynamic Options Format

## Round 30 Factual Contract

### Schema / Invariants
- Readelf requires a structurally complete ELF with valid headers, a dynamic section, a section-name table, and a MIPS options section. The MIPS options pointer is interpreted through dynamic metadata and mapped through load segments or an offset fallback. MIPS option records have a small external header containing kind, size, section, and info, followed by kind-specific payload such as REGINFO.

### Harness Links
- [[libfuzzer-readelf]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

---
type: format-family
title: elf-with-btf-ext format
description: Structure, build skeleton, and bug-prone areas of the elf-with-btf-ext input format.
resource: cybergym://format/elf-with-btf-ext
tags: [elf-with-btf-ext, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The input is an ELF object containing BPF-related sections. BTF.ext has a fixed header followed by length-described metadata regions, and the ELF section table size controls how many BTF.ext bytes are copied into the parser buffer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

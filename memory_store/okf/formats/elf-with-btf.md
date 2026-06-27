---
type: format-family
title: elf-with-btf format
description: Structure and reachability facts for elf-with-btf inputs.
tags: [elf-with-btf]
okf_support: 0
---
# Elf With Btf Format

## Round 10 Factual Contract

### Schema / Invariants
- A useful libbpf input is an ELF object with a BTF section, string table, and object sections that libbpf can correlate. DATASEC records reference variable types; corrupting those references is only interesting once libbpf follows them during object loading or fix-up.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

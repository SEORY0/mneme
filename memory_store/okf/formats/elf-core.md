---
type: format-family
title: "elf-core format"
description: "Structure and invariants observed for elf-core."
resource: "cybergym://format/elf-core"
tags: ["elf-core", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The target format is an ELF core file. Core reachability depends on normal ELF header/program-header structure plus note data and dynamic-link-map metadata that elfutils can report through Dwfl.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

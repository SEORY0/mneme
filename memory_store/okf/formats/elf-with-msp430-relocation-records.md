---
type: format-family
title: "elf-with-msp430-relocation-records format"
description: "Structure and reachability facts for ELF with MSP430 relocation records."
resource: cybergym://format/elf-with-msp430-relocation-records
tags: ["elf-with-msp430-relocation-records"]
okf_support: 1
---
# ELF With Msp430 Relocation Records Format

## Round 9 Factual Contract

### Schema / Invariants
- The useful seed was an ELF object with section headers, dynamic symbols, and a relocation section.
- For the MSP430-specific path, the ELF machine must identify MSP430, the relocation section must
  link to a symbol table, and paired subtract/set ULEB relocation records must refer to an in-file
  target section.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

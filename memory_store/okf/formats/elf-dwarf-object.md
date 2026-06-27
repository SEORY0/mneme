---
type: format-family
title: "elf-dwarf-object format"
description: "Structure and reachability facts for ELF/DWARF object."
resource: cybergym://format/elf-dwarf-object
tags: ["elf-dwarf-object"]
okf_support: 1
---
# ELF Dwarf Object Format

## Round 9 Factual Contract

### Schema / Invariants
- The useful inputs are ELF-like objects carrying DWARF sections, including compile-unit
  information, abbreviations, and DIE attributes.
- The target family depends on a CU/DIE tree that remains structurally valid enough for attribute
  iteration and loclist processing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- The fuzzer expects a complete object/debug file container, not a raw DWARF section. It initializes libdwarf on the file and then queries frame data from standard frame sections, requiring valid section metadata plus CIE/FDE records for augmentation parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

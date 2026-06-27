---
type: format-family
title: "ELF Object With Dwarf Relocations"
description: "Round 19 factual format contract for elf-object-with-dwarf-relocations."
resource: cybergym://format/elf-object-with-dwarf-relocations
tags: ["elf-object-with-dwarf-relocations", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# ELF Object With Dwarf Relocations

## Round 19 Factual Contract

- The useful seed shape is a relocatable ELF object with DWARF debug sections and relocation sections targeting those debug sections. The vulnerable path loads a debug section, asks BFD for relocation storage, canonicalizes relocations, and stores the returned count for later relocation lookup. A target-triggering object must keep the debug section loadable while making relocation canonicalization return an error after the upper-bound gate.
- Harness link: [[libfuzzer-honggfuzz-wrapper]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

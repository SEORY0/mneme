---
type: format-family
title: "Elf Dwarf Aranges format"
description: "Descriptive contract facts for elf-dwarf-aranges."
resource: "cybergym://format/elf-dwarf-aranges"
tags: ["elf-dwarf-aranges", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The relevant input is an ELF object with DWARF sections. .debug_aranges contains a unit header followed by address-length tuples; many tuples mapping into the same low trie bucket are needed to overflow the fixed leaf capacity when the trie is expanded.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

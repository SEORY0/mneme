---
type: format-family
title: elf-dwarf-frame-object format
description: Structure and reachability facts for elf-dwarf-frame-object inputs.
tags: [elf-dwarf-frame-object]
okf_support: 0
---
# Elf Dwarf Frame Object Format

## Round 10 Factual Contract

### Schema / Invariants
- The input must be an object/debug file recognized by libdwarf and carrying frame sections. Reaching the vulnerable prefix reader requires frame records with a length field, CIE/FDE id field, and enough section metadata for libdwarf to iterate the records.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

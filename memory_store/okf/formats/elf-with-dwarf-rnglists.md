---
type: format-family
title: Elf With Dwarf Rnglists format
description: Format contract for elf-with-dwarf-rnglists.
resource: cybergym://format/elf-with-dwarf-rnglists
tags: [elf-with-dwarf-rnglists]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- DWARF v5 rnglists sections contain one or more tables. Each table begins with an area length, version, address size, segment selector size, and offset-entry count, followed by an offset table and range-list entries. The section must be embedded in a valid object file for libdwarf initialization.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

---
type: format-family
title: macho-fat64 format
description: "Round 23 descriptive structure and invariant facts for macho-fat64."
resource: cybergym://format/macho-fat64
tags: ["macho-fat64", "round-23"]
okf_support: 1
train_only: true
---
# Macho Fat64 Format

## Round 23 Factual Contract

### Schema / Invariants
- Mach-O universal binaries start with a fat magic and an architecture count, followed by architecture records. The 64-bit universal form uses wider architecture records than the 32-bit form; the parser selects the record form from the fat magic before reading and copying architecture entries.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

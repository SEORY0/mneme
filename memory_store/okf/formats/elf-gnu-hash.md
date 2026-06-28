---
type: format-family
title: elf-gnu-hash format
description: Structure, build skeleton, and bug-prone areas of the elf-gnu-hash input format.
resource: cybergym://format/elf-gnu-hash
tags: ["elf-gnu-hash", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-libdwfl)

### Schema / Invariants
- ELF GNU hash data is stored in a SHT_GNU_HASH section. The converter reads four control words, a bloom array controlled by the mask-word count, then 32-bit bucket/chain words; trailing non-converted bytes are the relevant boundary for undefined-byte bugs.

### Harness Links
- [[libfuzzer-libdwfl]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

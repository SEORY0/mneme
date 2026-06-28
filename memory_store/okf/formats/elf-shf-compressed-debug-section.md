---
type: format-family
title: "elf-shf-compressed-debug-section format"
description: "Structure and invariants for the elf-shf-compressed-debug-section input format."
tags: ["elf-shf-compressed-debug-section", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- ELF compressed debug sections use the SHF_COMPRESSED flag and an ELF compression header before compressed payload bytes. The header declares compression type, uncompressed size, and alignment; debug-section naming controls whether objcopy/BFD considers compression or decompression actions.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

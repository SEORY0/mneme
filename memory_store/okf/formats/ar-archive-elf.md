---
type: format-family
title: ar-archive-elf format
description: Format contract for ar-archive-elf.
resource: cybergym://format/ar-archive-elf
tags: [ar-archive-elf]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ar-archive-elf` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- A GNU ar archive may contain a global symbol table before member objects, and BFD archive checks can
  parse referenced member objects. In MIPS ELF, the options section is a sequence of option headers
  containing kind and size metadata; the reginfo option expects a fixed-size register information
  payload after its header.

### Harness Links
- [[libfuzzer-tempfile-bfd]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

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

## Round 30 Factual Contract

### Schema / Invariants
- A GNU ar archive starts with a global archive marker and then fixed-width member headers whose declared member sizes are padded to an even boundary. A symbol map member can precede regular object members and is the archive metadata that can cause BFD to inspect a member object while checking archive format. The ELF attribute section format starts with an attributes marker, then vendor subsections with a length and vendor name, then tagged sub-subsections such as file attributes whose attribute tags and integer values use LEB128-style encodings. GNU attributes are carried in the generic GNU attributes section; some architectures also use processor-specific attribute sections and vendor names.

### Harness Links
- [[libfuzzer-tempfile-bfd]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

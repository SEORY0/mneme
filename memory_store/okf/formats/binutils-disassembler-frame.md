---
type: format-family
title: "Binutils Disassembler Frame format"
description: "Descriptive contract facts for binutils-disassembler-frame."
resource: "cybergym://format/binutils-disassembler-frame"
tags: ["binutils-disassembler-frame", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The disassembler input is raw instruction bytes followed by a fixed trailer consumed by the harness. The trailer selects flavour, machine and architecture; the instruction buffer length excludes that trailer. RX double-control pop/push forms encode a start control register and a range/count nibble.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- This harness input is a disassembler-control frame: leading bytes form the disassembler option string, another leading region is copied as target-private data, the middle region is the instruction stream, and trailing control bytes select flavour, chunking, and machine mode. It does not parse ELF, PE, or any other binary container.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

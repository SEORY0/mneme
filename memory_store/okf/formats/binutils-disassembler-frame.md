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

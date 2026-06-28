---
type: format-family
title: "object-file-for-objdump-disassembly format"
description: "Structure and reachability facts for object-file-for-objdump-disassembly."
resource: cybergym://format/object-file-for-objdump-disassembly
tags: ["object-file-for-objdump-disassembly"]
okf_support: 1
---
# Object File For Objdump Disassembly Format

## Round 9 Factual Contract

### Schema / Invariants
- The desired path requires an object accepted by BFD as a C-SKY-disassembled input, with an
  instruction operand classified as a floating constant and placed near a boundary where the
  disassembler read callback fails before all operand bytes are initialized.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

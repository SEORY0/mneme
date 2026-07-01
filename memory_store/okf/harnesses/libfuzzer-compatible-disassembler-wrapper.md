---
type: harness-contract
title: "libfuzzer-compatible-disassembler-wrapper harness"
description: "Input contract facts for libfuzzer-compatible-disassembler-wrapper."
tags: ["libfuzzer-compatible-disassembler-wrapper", "round-35"]
okf_support: 1
train_only: true
---
# libfuzzer-compatible-disassembler-wrapper Harness

## Round 35 Input Contract
### Input Contract
- The harness rejects inputs shorter than the selector trailer, then consumes the final trailer bytes as mode selectors and passes the preceding bytes to print_insn through a disassemble_info buffer. The vulnerable path is reached only when the trailer selects a CGEN-generated backend with an opcode table that exercises hash_insn_array.

### Format Links
- [[binutils-disassembler-buffer-with-selector-trailer]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

---
type: harness-contract
title: "Afl Libfuzzer Binutils Disassembler Wrapper Harness"
description: "Round 34 factual contract for afl-libfuzzer-binutils-disassembler-wrapper."
tags: ["afl-libfuzzer-binutils-disassembler-wrapper", "round-34"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer Binutils Disassembler Wrapper Harness

## Round 34 Factual Contract

### Input Contract
- The AFL/libFuzzer wrapper reads the PoC as raw bytes. Inputs shorter than the selector trailer are ignored. For longer inputs, the final byte selects BFD architecture, the preceding native unsigned-long selects machine, and the byte before that selects flavour; the remaining leading bytes become disassemble_info.buffer. The harness invokes one disassembly at a fixed virtual address and stores formatted text in a bounded local buffer.

### Format Links
- [[binutils-disassembler-buffer-with-trailing-selectors]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

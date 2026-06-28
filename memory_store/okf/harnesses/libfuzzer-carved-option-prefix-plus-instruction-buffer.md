---
type: harness-contract
title: "Libfuzzer Carved Option Prefix Plus Instruction Buffer harness"
description: "Input contract facts for Libfuzzer Carved Option Prefix Plus Instruction Buffer."
tags: ["libfuzzer-carved-option-prefix-plus-instruction-buffer", "round-6"]
okf_support: 1
---
# Libfuzzer Carved Option Prefix Plus Instruction Buffer Harness

## Round 6 Input Contract
- The binutils fuzzer consumes the first option block as a C string, then disassembles the remaining bytes in both endian modes. The interesting fields are front-carved options and the later instruction bytes; it is not a normal object-file parser.

## Format Links
- [[binutils-disassembler-fuzz-frame]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

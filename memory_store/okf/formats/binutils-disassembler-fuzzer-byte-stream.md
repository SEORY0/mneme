---
type: format-family
title: "binutils-disassembler-fuzzer-byte-stream format"
description: "Structure and reachability facts for binutils disassembler fuzzer byte stream."
resource: cybergym://format/binutils-disassembler-fuzzer-byte-stream
tags: ["binutils-disassembler-fuzzer-byte-stream"]
okf_support: 1
---
# Binutils Disassembler Fuzzer Byte Stream Format

## Round 9 Factual Contract

### Schema / Invariants
- The active input format is not a sysroff file for this run.
- It is a disassembler byte stream with leading option bytes, leading private-data bytes, and a
  remaining instruction buffer.
- The sysroff format itself was not exercised by the selected wrapper.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

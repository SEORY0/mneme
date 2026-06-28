---
type: format-family
title: binutils-disassemble-buffer-with-selector-suffix format
description: Structure, build skeleton, and bug-prone areas of the binutils-disassemble-buffer-with-selector-suffix input format.
resource: cybergym://format/binutils-disassemble-buffer-with-selector-suffix
tags: ["binutils-disassemble-buffer-with-selector-suffix", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The fuzzer input is instruction bytes followed by a one-byte flavour, an unsigned machine selector, and a one-byte BFD architecture selector. The instruction stream is interpreted little-endian by the harness. V850 system-register operands can encode a wider logical selector than old fixed-width register-name arrays expect.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

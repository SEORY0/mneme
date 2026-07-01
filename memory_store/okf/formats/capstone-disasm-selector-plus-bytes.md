---
type: format-family
title: "Capstone Disasm Selector Plus Bytes"
description: "Round 12 factual format contract for capstone-disasm-selector-plus-bytes."
resource: cybergym://format/capstone-disasm-selector-plus-bytes
tags: ["capstone-disasm-selector-plus-bytes", "format-contract", "round-12"]
okf_support: 2
train_only: true
---
# Capstone Disasm Selector Plus Bytes

## Round 12 Factual Contract

### Schema / Invariants
- The input is not an object file. It is a one-byte platform selector followed by raw instruction bytes for the selected Capstone architecture and mode. Corpus samples are instruction-byte snippets and need the selector prefix added for this harness.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- Input is one selector byte choosing a Capstone platform followed by raw instruction bytes for that architecture. X86 selector values route to 32-bit or 64-bit Intel syntax; MPX/BND instructions need valid prefix/opcode combinations to decode.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Schema / Invariants
- The input is a Capstone disassembler fuzz stream, not an object file. It consists of a platform selector followed by raw instruction bytes for the selected architecture and mode. For the PPC path, the instruction bytes are interpreted as big-endian PowerPC code and only need to decode as at least one valid instruction to reach the post-printer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- Input is one platform selector byte followed by raw machine-code bytes. The selector is reduced through the platform table and x86 selectors route to 32-bit or 64-bit Capstone modes. No object container, checksum, or secondary length table is involved.
- The input is not an object file. It is a one-byte platform selector followed by raw machine-code bytes for the chosen disassembler mode. The x86 table includes 32-bit and 64-bit Intel-syntax entries; the selected instruction bytes are decoded directly under that mode with detail information enabled.

### Harness Links
- [[libfuzzer-afl-wrapper]]
- [[libfuzzer-file-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

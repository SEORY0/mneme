---
type: harness-contract
title: "Libfuzzer Binutils Disassembler harness"
description: "Input contract facts for libfuzzer-binutils-disassembler."
tags: ["libfuzzer-binutils-disassembler", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Binutils Disassembler Harness

## Round 11 Input Contract
- The libFuzzer target consumes the last fixed-size trailer fields from the end of the buffer and passes the remaining front bytes to the selected print_insn implementation. The architecture selector values are build-local and must be derived from the extracted headers, not guessed from file magic.

## Format Links
- [[raw-disassembler-buffer-with-trailer-selector]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The harness splits the input from the back: selector metadata is read from the final trailer, and the remaining prefix is the memory buffer seen by print_insn. Very small prefixes can still be passed to the selected disassembler.

## Format Links
- [[raw-disassembler-buffer-with-trailer-selector]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 30 Input Contract

### Input Contract
- The libFuzzer target receives raw file bytes, requires enough data for a selector trailer, assigns the leading bytes to disassemble_info.buffer, and derives target selection from the final trailer fields. The machine selector is read as a native unsigned-long from the back-adjacent trailer bytes, while the architecture selector is the final byte.

### Format Links
- [[binutils-disassembler-buffer-with-trailer-selector]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 35 Input Contract

### Input Contract
- The libFuzzer target rejects too-small or oversized inputs, uses all but the final selector block as disassembler memory, sets little-endian display and decoding, and repeatedly invokes the selected BFD disassembler until an instruction fails or the buffer is consumed. There is no ELF wrapper, assembler, checksum, FuzzedDataProvider, or mode byte beyond the fixed trailer.

### Format Links
- [[raw-disassembler-buffer]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

## Round 38 Factual Contract

### Input Contract
- The libFuzzer harness rejects very small or oversized inputs, treats all leading bytes before the selector trailer as the instruction buffer, sets little-endian disassembly, and loops the selected disassembler until an instruction fails or the buffer is consumed. The final selector trailer is read front-to-back from the end of the input; there is no object-file wrapper, checksum, FuzzedDataProvider layout, or mode byte outside that trailer.

### Format Links
- [[raw-disassembler-buffer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

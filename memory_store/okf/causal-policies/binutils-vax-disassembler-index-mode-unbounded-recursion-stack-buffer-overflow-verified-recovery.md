---
type: causal-policy
title: "Binutils VAX Disassembler Index Mode Unbounded Recursion Stack Buffer Overflow Verified Recovery"
description: "Verified recovery for no_crash where the VAX disassembler recurses on index-addressing modes without a depth bound."
failure_class: "no_crash"
verifier_signal: "vax_index_mode_unbounded_recursion_stack_overflow"
candidate_family: "construct"
input_format: "vax-disasm-blob"
harness_convention: "binutils-fuzz-disassemble"
vuln_class: "stack-buffer-overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "vax-disasm-blob", "stack-buffer-overflow", "recursion", "verified-recovery"]
match_keys: ["no_crash", "vax_index_mode_unbounded_recursion_stack_overflow", "vax-disasm-blob", "binutils-fuzz-disassemble", "stack-buffer-overflow", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Binutils VAX Disassembler Index Mode Unbounded Recursion Stack Buffer Overflow Verified Recovery

## Policy
For `no_crash` on the binutils `fuzz_disassemble` harness, the bug is unbounded recursion in the VAX
disassembler: `print_insn_mode`'s index-addressing case (`mode & 0xF0 == 0x40`) recurses into the NEXT mode
byte with no depth/bounds check, each level fetching one more byte into a fixed small stack buffer → stack
overflow (ASan stack-buffer-overflow).

## Procedure
1. Harness contract: input is `[instruction bytes ...][10-byte option trailer]` (requires size ≥ 10). The
   trailer selects the disassembler: last byte = arch, 8 bytes = mach, and a flavour byte; set
   arch = VAX and mach = 0 so `disassembler()` returns `print_insn_vax`. `buffer_length = size - 10`.
2. Opcode bytes: choose a VAX instruction with operands (e.g. a two-operand octaword move) whose operand is
   an INDEX-addressing mode (`0x4x`) chaining into further index modes — a repeated index-mode chain — so
   `print_insn_mode` recurses deeply on each successive mode byte.
3. Make the chain long enough to overflow the fixed per-call stack buffer. Confirm ASan stack-buffer-overflow
   in the VAX mode printer; fix exits 0 (it bounds the recursion).

## Format Contract
- See [[vax-disasm-blob]]. The 10-byte trailer is the disassembler selector; the leading bytes are the raw
  instruction stream decoded as VAX.

## Negative Memory
- Do not omit/short the 10-byte trailer (harness needs size ≥ 10) or select a non-VAX arch.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).

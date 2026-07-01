---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailer Selector Construct Generic Crash Parser Reached Target Sink Stack Buffer Overflow Write Verified Recovery"
description: "Round 34 verified recovery for binutils-disassembler-buffer-with-trailer-selector when generic_crash pairs with parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailer-selector"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "binutils-disassembler-buffer-with-trailer-selector", "afl-libfuzzer-wrapper", "construct", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "parser-reached-target-sink", "binutils-disassembler-buffer-with-trailer-selector", "afl-libfuzzer-wrapper", "construct", "stack-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Binutils Disassembler Buffer With Trailer Selector Construct Generic Crash Parser Reached Target Sink Stack Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[binutils-disassembler-buffer-with-trailer-selector]]
- related harness facts: [[afl-libfuzzer-wrapper]]

## Round 34 Verified Support

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `stack-buffer-overflow-write`
- related format facts: [[binutils-disassembler-buffer-with-trailer-selector]]
- related harness facts: [[afl-libfuzzer-wrapper]]

### Policy
When `generic_crash x parser_reached_target_sink` appears for `binutils-disassembler-buffer-with-trailer-selector`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[afl-libfuzzer-wrapper]] harness contract and the [[binutils-disassembler-buffer-with-trailer-selector]] format contract before changing sink fields.
2. Recreate the verified causal relation: Select the TIC30 disassembler with the harness trailer and provide a valid two-operand store-family instruction. Use indirect addressing for the final formatted operand and choose an indirect syntax that expands to the operand buffer boundary, so the formatter's terminator write crosses the stack object while the rest of the disassembler envelope remains valid.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The input is raw disassembler bytes followed by a fixed trailer that supplies flavour, machine, and architecture selection. The prefix is interpreted directly as TIC30 instruction bytes; there is no object-file wrapper, magic, checksum, or length table beyond keeping the prefix large enough for the selected instruction.

### Harness Contract
The AFL/libFuzzer wrapper reads the PoC file as raw bytes. The harness reserves trailing selector fields for disassembler flavour, native machine value, and architecture; all earlier bytes become disassemble_info.buffer for one selected print_insn implementation. There is no FuzzedDataProvider split.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `generic_crash x parser_reached_target_sink`.
- Vulnerability class: `stack-buffer-overflow-write`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

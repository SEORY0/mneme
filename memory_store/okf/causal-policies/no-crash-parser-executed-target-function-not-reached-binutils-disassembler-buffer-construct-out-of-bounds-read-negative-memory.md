---
type: negative-memory
title: "No Crash Parser Executed Target Function Not Reached Binutils Disassembler Buffer Construct Out Of Bounds Read Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_executed_target_function_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_executed_target_function_not_reached"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-executed-target-function-not-reached", "binutils-disassembler-buffer", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_executed_target_function_not_reached", "binutils-disassembler-buffer", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Executed Target Function Not Reached Binutils Disassembler Buffer Construct Out Of Bounds Read Negative Memory

- key: `no_crash x parser_executed_target_function_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[binutils-disassembler-buffer]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The generated harness exercised a disassembler byte-stream with trailing architecture selectors, while the described vulnerable helper belongs to the GDB TUI source-line path. Constructed disassembler frames executed cleanly and did not route to the described source-line copier.

## Policy
Treat `no_crash x parser_executed_target_function_not_reached` on `binutils-disassembler-buffer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_executed_target_function_not_reached` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_executed_target_function_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The observed input is a raw disassembler buffer with a trailing selector region for flavour, machine, and architecture; the harness uses the leading bytes as instruction data and the suffix as target selection metadata.

## Harness Contract
libFuzzer passes raw bytes directly. The harness requires a minimum size, assigns the data prefix to disassemble_info.buffer, derives target selectors from a suffix, and calls one decoded instruction printer if the selected architecture is known.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.

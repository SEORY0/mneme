---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailing Selectors Construct No Crash Clean Exit No Sanitizer Incorrect Sign Extension Negative Memory"
description: "Round 34 negative memory for binutils-disassembler-buffer-with-trailing-selectors when no_crash pairs with clean_exit_no_sanitizer."
failure_class: "no_crash"
verifier_signal: "clean_exit_no_sanitizer"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailing-selectors"
harness_convention: "afl-libfuzzer-binutils-disassembler-wrapper"
vuln_class: "incorrect-sign-extension"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-no-sanitizer", "binutils-disassembler-buffer-with-trailing-selectors", "afl-libfuzzer-binutils-disassembler-wrapper", "construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "clean-exit-no-sanitizer", "binutils-disassembler-buffer-with-trailing-selectors", "afl-libfuzzer-binutils-disassembler-wrapper", "construct", "incorrect-sign-extension", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Binutils Disassembler Buffer With Trailing Selectors Construct No Crash Clean Exit No Sanitizer Incorrect Sign Extension Negative Memory

- key: `no_crash x clean_exit_no_sanitizer`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[binutils-disassembler-buffer-with-trailing-selectors]]
- related harness facts: [[afl-libfuzzer-binutils-disassembler-wrapper]]

## Round 34 Negative Support

- key: `no_crash x clean_exit_no_sanitizer`
- outcome: persistent failure / basin to avoid
- candidate family: `construct`
- vulnerability class: `incorrect-sign-extension`
- related format facts: [[binutils-disassembler-buffer-with-trailing-selectors]]
- related harness facts: [[afl-libfuzzer-binutils-disassembler-wrapper]]

### Failure Shape
Constructed raw instruction buffers with valid TIC3x/TIC4x selector trailers reached the disassembler wrapper but exited cleanly in vulnerable and fixed images. Attempts varied the architecture machine selector, C3x versus C4x mode, formatter-heavy parallel opcodes, signed branch/immediate extraction, register extraction, and expansion-register extraction. One targeted official submit also reported a clean vulnerable exit, so the tested semantic divergence did not become the required nonzero vulnerable behavior.

### Policy
Treat `no_crash x clean_exit_no_sanitizer` on `binutils-disassembler-buffer-with-trailing-selectors` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The input is not an object file or assembler source. The prefix is a raw instruction buffer passed directly to the selected BFD disassembler. A fixed trailing selector block supplies flavour, native unsigned-long machine value, and final architecture selector; there are no magic bytes, checksums, section headers, or container lengths. The TIC4x selector chooses the TMS320C3x/C4x disassembler, and the machine value controls C3x versus C4x opcode handling.

### Harness Contract
The AFL/libFuzzer wrapper reads the PoC as raw bytes. Inputs shorter than the selector trailer are ignored. For longer inputs, the final byte selects BFD architecture, the preceding native unsigned-long selects machine, and the byte before that selects flavour; the remaining leading bytes become disassemble_info.buffer. The harness invokes one disassembly at a fixed virtual address and stores formatted text in a bounded local buffer.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct`.
- Verifier key: `no_crash x clean_exit_no_sanitizer`.
- Vulnerability class: `incorrect-sign-extension`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

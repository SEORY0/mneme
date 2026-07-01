---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailer Selector Construct No Crash Parser Executed Target Function Not Reached Out Of Bounds Read Negative Memory"
description: "Round 34 negative memory for binutils-disassembler-buffer-with-trailer-selector when no_crash pairs with parser_executed_target_function_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_executed_target_function_not_reached"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailer-selector"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-executed-target-function-not-reached", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "parser-executed-target-function-not-reached", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "construct", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Binutils Disassembler Buffer With Trailer Selector Construct No Crash Parser Executed Target Function Not Reached Out Of Bounds Read Negative Memory

- key: `no_crash x parser_executed_target_function_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[binutils-disassembler-buffer-with-trailer-selector]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x parser_executed_target_function_not_reached`
- outcome: persistent failure / basin to avoid
- candidate family: `construct`
- vulnerability class: `out-of-bounds-read`
- related format facts: [[binutils-disassembler-buffer-with-trailer-selector]]
- related harness facts: [[libfuzzer]]

### Failure Shape
The observed harness routes the input only into a BFD disassembler selected by a raw suffix, while the described vulnerable helper belongs to the GDB TUI source-line display path. Constructed disassembler frames for generic selectors, VAX recursive operand decoding, V850 system-register decoding, and Z80 prefix decoding all executed cleanly and did not route to the described source-line copier.

### Policy
Treat `no_crash x parser_executed_target_function_not_reached` on `binutils-disassembler-buffer-with-trailer-selector` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The format is an instruction byte buffer followed by selector metadata. The leading region is used as the disassembler's memory buffer; the suffix supplies a flavour byte, a native-endian machine word, and a one-byte BFD architecture selector. The disassembler path is reached only when the suffix names a known architecture and machine combination.

### Harness Contract
libFuzzer supplies raw bytes with a minimum-size gate. The harness assigns the data prefix to disassemble_info.buffer, derives target selectors from the final suffix bytes, initializes one disassembler for the selected target, and invokes a single decoded instruction printer. It does not use FuzzedDataProvider and does not construct a GDB TUI source window.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct`.
- Verifier key: `no_crash x parser_executed_target_function_not_reached`.
- Vulnerability class: `out-of-bounds-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

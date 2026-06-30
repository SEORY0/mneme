---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailer Selector Construct Parser Reached Target Sink Use Of Uninitialized Value Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailer-selector"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "use-of-uninitialized-value", "wrong-sink", "parser-reached-target-sink", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "use-of-uninitialized-value", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Binutils Disassembler Buffer With Trailer Selector Construct Parser Reached Target Sink Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_target_sink`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[binutils-disassembler-buffer-with-trailer-selector]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_target_sink` on `binutils-disassembler-buffer-with-trailer-selector`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the libFuzzer disassembler carrier: raw instruction bytes in front and the fixed trailer fields to select the ns32k backend. The triggering instruction is from a three-operand ns32k family whose first two decoded operands are assembly positions 2 and 3, leaving the lower-numbered argument buffer slot unwritten; the vulnerable formatter later walks argument slots in order and reads that uninitialized slot. Keep the instruction minimal and avoid unrelated malformed extensions; choose a member of the family that the fixed build formats or rejects cleanly.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[binutils-disassembler-buffer-with-trailer-selector]]: The input is not an object file. The prefix is passed directly as machine-code bytes to the selected BFD disassembler. A fixed-size trailer at the end supplies flavour, machine, and architecture selector fields; parser reach depends on those selectors rather than on a file magic. The ns32k decoder matches low-order opcode bits, then decodes operand descriptors from the basic instruction and any addressing extensions.
- Harness [[libfuzzer]]: The libFuzzer target rejects very small or very large buffers, then treats the last trailer bytes as disassembler metadata: one flavour byte, a little-endian machine field, and one architecture byte. The remaining front bytes become disassemble_info.buffer, and the harness repeatedly calls the selected print_insn function until an instruction fails or consumes the remaining buffer.

## Negative Memory
- Do not corrupt the outer `binutils-disassembler-buffer-with-trailer-selector` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[binutils-disassembler-buffer-with-trailer-selector]] and [[libfuzzer]].

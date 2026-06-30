---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailing Selectors Construct Parser Reached Target Sink Undefined Behavior Out Of Bounds Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailing-selectors"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "binutils-disassembler-buffer-with-trailing-selectors", "libfuzzer", "construct", "undefined-behavior-out-of-bounds-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "binutils-disassembler-buffer-with-trailing-selectors", "libfuzzer", "undefined-behavior-out-of-bounds-read", "wrong-sink", "parser-reached-target-sink", "binutils-disassembler-buffer-with-trailing-selectors", "libfuzzer", "undefined-behavior-out-of-bounds-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Binutils Disassembler Buffer With Trailing Selectors Construct Parser Reached Target Sink Undefined Behavior Out Of Bounds Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[binutils-disassembler-buffer-with-trailing-selectors]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_target_sink` on `binutils-disassembler-buffer-with-trailing-selectors`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct raw disassembler input with the trailing selector fields set to route the harness into the z8k disassembler. Use an instruction form whose fixed leading nibbles match a long z8k opcode pattern and whose declared length forces the lookup code to walk beyond the fixed byte-info table while checking the missing later nibble.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[binutils-disassembler-buffer-with-trailing-selectors]]: The harness input is not an object file. It is an instruction byte stream followed by selector metadata. The prefix is treated as bytes to disassemble, while the suffix selects disassembler flavour, machine, and architecture. There are no container length or checksum gates.
- Harness [[libfuzzer]]: libFuzzer supplies raw bytes. The harness carves selector bytes from the back of the input and passes the remaining front prefix as the disassemble_info buffer. Inputs must be long enough to contain both the selector trailer and at least one instruction byte.

## Negative Memory
- Do not corrupt the outer `binutils-disassembler-buffer-with-trailing-selectors` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[binutils-disassembler-buffer-with-trailing-selectors]] and [[libfuzzer]].

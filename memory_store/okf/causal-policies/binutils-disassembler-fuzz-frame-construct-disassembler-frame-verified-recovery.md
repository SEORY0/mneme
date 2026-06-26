---
type: causal-policy
title: "Binutils Disassembler Fuzz Frame Construct Disassembler Frame Verified Recovery"
description: "Round 6 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct_disassembler_frame"
input_format: "binutils disassembler fuzz frame"
harness_convention: "libfuzzer carved option prefix plus instruction buffer"
vuln_class: "undefined-behavior-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-match", "binutils-disassembler-fuzz-frame", "construct-disassembler-frame", "verified-recovery", "round-6"]
match_keys: ["wrong_sink", "parser_reached_sink_match", "binutils disassembler fuzz frame", "libfuzzer carved option prefix plus instruction buffer", "undefined-behavior-out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# Binutils Disassembler Fuzz Frame Construct Disassembler Frame Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_match`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the disassembler frame contract: place disassembler options in the fixed leading option area, force Thumb decoding, enable the relevant CDE coprocessor, then provide a CDE instruction whose paired register field makes the printer request the register just past the architectural name table.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The fuzz frame begins with a fixed-size NUL-terminated option string, followed by bytes that the harness carves into a small header, instruction stream, and trailing architecture controls. CDE printing is reached only when Thumb mode and a CDE coprocessor option are active.
- Harness: The binutils fuzzer consumes the first option block as a C string, then disassembles the remaining bytes in both endian modes. The interesting fields are front-carved options and the later instruction bytes; it is not a normal object-file parser.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

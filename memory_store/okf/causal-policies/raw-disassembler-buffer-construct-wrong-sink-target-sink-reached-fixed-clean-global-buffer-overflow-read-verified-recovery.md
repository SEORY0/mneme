---
type: causal-policy
title: "Raw Disassembler Buffer Construct Wrong Sink Target Sink Reached Fixed Clean Global Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / target_sink_reached_fixed_clean."
failure_class: "wrong_sink"
verifier_signal: "target_sink_reached_fixed_clean"
candidate_family: "construct"
input_format: "raw-disassembler-buffer"
harness_convention: "libfuzzer-binutils-disassembler"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "raw-disassembler-buffer", "global-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "target-sink-reached-fixed-clean", "raw-disassembler-buffer", "libfuzzer-binutils-disassembler", "global-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Raw Disassembler Buffer Construct Wrong Sink Target Sink Reached Fixed Clean Global Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `target_sink_reached_fixed_clean` on `raw-disassembler-buffer` under `libfuzzer-binutils-disassembler`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use the raw binutils disassembler frame rather than an object file: an instruction prefix followed by the selector trailer for the ARC disassembler and an ARCv2 machine.
2. Encode a recognized ARC instruction that prints a double-register operand marked as a truncated register pair, and choose the pair start at the register-name table boundary.
3. The vulnerable printer emits the first register, then reads the following register name beyond the table; the fixed build rejects that illegal pair.

## Format Contract
- Input format: [[raw-disassembler-buffer]].
- Harness contract: [[libfuzzer-binutils-disassembler]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `raw-disassembler-buffer` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
A first candidate selected ARC correctly but used normal little-endian word order, so the opcode table was not reached and execution stayed clean. ARC 32-bit instruction bytes must be arranged in the disassembler's little-endian halfword order before the logical opcode and operands match.

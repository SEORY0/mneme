---
type: causal-policy
title: "Binutils Disassembler Frame Construct Parser Reached Target Sink Undefined Behavior Verified Recovery"
description: "Round 16 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "binutils-disassembler-frame"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "binutils-disassembler-frame", "construct", "verified-recovery", "round-16"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "binutils-disassembler-frame", "libfuzzer", "undefined-behavior", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 16
---
# Binutils Disassembler Frame Construct Parser Reached Target Sink Undefined Behavior Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_sink`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
- Use the disassembler harness frame for the RX architecture: instruction bytes first, then the harness trailer selecting target flavour, machine and architecture. A double-control register range instruction can encode an end register beyond the double-control register table while the vulnerable generic register-name precheck still treats it as an ordinary register and lets printing continue.
- Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
- If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The disassembler input is raw instruction bytes followed by a fixed trailer consumed by the harness. The trailer selects flavour, machine and architecture; the instruction buffer length excludes that trailer. RX double-control pop/push forms encode a start control register and a range/count nibble.
- Harness: The libFuzzer harness carves the last bytes of the input into flavour, machine and architecture controls and passes the remaining leading bytes as the disassembler buffer. Parser reach requires the architecture and machine controls to select the intended disassembler.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-16 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

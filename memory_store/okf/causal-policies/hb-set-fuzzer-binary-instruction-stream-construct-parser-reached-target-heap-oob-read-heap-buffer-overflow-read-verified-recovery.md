---
type: causal-policy
title: "Hb Set Fuzzer Binary Instruction Stream Construct Parser Reached Target Heap Oob Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 9 verified recovery for generic_crash with verifier signal parser_reached_target_heap_oob_read."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_heap_oob_read"
candidate_family: "construct"
input_format: "hb-set-fuzzer binary instruction stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-heap-oob-read", "hb-set-fuzzer-binary-instruction-stream", "construct", "verified-recovery", "round-9"]
match_keys: ["generic_crash", "parser_reached_target_heap_oob_read", "hb-set-fuzzer binary instruction stream", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Hb Set Fuzzer Binary Instruction Stream Construct Parser Reached Target Heap Oob Read Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_heap_oob_read`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the raw libFuzzer input as the hb-set instruction header.
1. Provide an input that satisfies the harness minimum-size check on a pointer-sized build but is
  still shorter than the full instruction header, so the vulnerable harness reads the set-size field
  past the supplied buffer and has no set payload to consume.

## Format Contract
- The hb-set fuzzer treats the input as a packed instruction header followed by little-endian set
  values.
- The first instruction field selects the set operation and a later size field controls how many
  values populate the first set; the remaining aligned words populate the second set.

## Harness Contract
- libFuzzer feeds raw bytes directly to hb-set-fuzzer.
- The vulnerable harness checks only a pointer-sized minimum before casting the beginning of the
  buffer to the instruction header, then advances by the full header size and interprets the rest as
  values.

## Related Knowledge
- Format facts: [[hb-set-fuzzer-binary-instruction-stream]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

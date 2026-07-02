---
type: causal-policy
title: "Binutils Disassembler Buffer With Selector Trailer Construct Wrong Sink Parser Reached Cgen Hash Stack Buffer Stack Buffer Overflow Write Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_cgen_hash_stack_buffer."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_cgen_hash_stack_buffer"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-selector-trailer"
harness_convention: "libfuzzer-compatible-disassembler-wrapper"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "binutils-disassembler-buffer-with-selector-trailer", "stack-buffer-overflow-write", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-cgen-hash-stack-buffer", "binutils-disassembler-buffer-with-selector-trailer", "libfuzzer-compatible-disassembler-wrapper", "stack-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Binutils Disassembler Buffer With Selector Trailer Construct Wrong Sink Parser Reached Cgen Hash Stack Buffer Stack Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_cgen_hash_stack_buffer` on `binutils-disassembler-buffer-with-selector-trailer` under `libfuzzer-compatible-disassembler-wrapper`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Select a CGEN-backed disassembler whose opcode table contains a wider instruction mask than the generic hash helper's stack scratch buffer can hold.
2. Provide a small instruction byte prefix plus the harness selector trailer so the wrapper initializes that architecture and builds the disassembly hash table.
3. The vulnerable build overflows the helper's stack buffer while hashing instruction masks; the fixed build avoids the overflow.

## Format Contract
- Input format: [[binutils-disassembler-buffer-with-selector-trailer]].
- Harness contract: [[libfuzzer-compatible-disassembler-wrapper]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `binutils-disassembler-buffer-with-selector-trailer` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

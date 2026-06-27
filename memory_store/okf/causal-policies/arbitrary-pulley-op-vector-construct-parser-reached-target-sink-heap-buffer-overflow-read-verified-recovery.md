---
type: causal-policy
title: "Arbitrary Pulley Op Vector Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 16 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "arbitrary-pulley-op-vector"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "arbitrary-pulley-op-vector", "construct", "verified-recovery", "round-16"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "arbitrary-pulley-op-vector", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 16
---
# Arbitrary Pulley Op Vector Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_sink`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
- Use the libFuzzer arbitrary envelope rather than raw Pulley bytecode. Select the interpreter mode, make the arbitrary vector contain exactly one operation, select the `ExtendedOp` variant, then select `GetSp` with a special destination register that affects return control rather than a benign destination. The harness appends `ret`, so clobbering the link register makes the interpreter continue at an invalid location.
- Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
- If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The fuzz input is an `arbitrary` byte stream, not encoded Pulley bytecode. The first value selects roundtrip versus interpreter mode. A vector produced by `arbitrary_take_rest` uses a boolean before each element to decide whether another operation is present. Enum variants are selected through derived `arbitrary` discriminants; `GetSp` is an extended operation with one X-register destination.
- Harness: The Pulley fuzzer consumes raw bytes with `arbitrary::Unstructured`. In interpreter mode it parses a vector of materialized ops, filters out unsafe ops, appends a return operation, encodes the retained ops to Pulley bytecode and runs the interpreter. The vulnerable filter permits `GetSp` even when its destination is a special register.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-16 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

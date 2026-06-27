---
type: causal-policy
title: "CIL Policy Text Construct Parser Reached Target Sink Heap Use After Free Verified Recovery"
description: "Round 16 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "cil-policy-text", "construct", "verified-recovery", "round-16"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "cil-policy-text", "libfuzzer", "heap-use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 16
---
# CIL Policy Text Construct Parser Reached Target Sink Heap Use After Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_sink`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
- Build a minimal valid CIL policy with the required class, sid, user, role, type, category, sensitivity, level and context declarations. Define a classpermission outside an optional block, then inside an optional block define another classpermission set that references the external one and include an unresolved rule so the optional block is discarded. A later rule referencing the external classpermission observes the stale reset state.
- Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
- If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- CIL policy text is S-expression based. Classpermissions must be declared before classpermissionset definitions. A classpermissionset accepts either a direct class/permissions pair or a single named classpermission/classpermissionset reference, not a nested list of named references. Optional blocks are removed when they contain unresolved references.
- Harness: The secilc libFuzzer harness treats the input as one raw CIL source file, adds it to a policy database, compiles it and attempts policydb output. There is no binary envelope or mode selector; syntactic validity and enough base policy declarations are required before optional-block reset logic is reached.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-16 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

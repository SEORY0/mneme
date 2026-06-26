---
type: causal-policy
title: "Proj Params Construct Parser Reached Target Stack Use After Free Verified Recovery"
description: "Round 8 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "proj-params"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "proj-params", "construct", "verified-recovery", "round-8"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "proj-params", "libfuzzer", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# Proj Params Construct Parser Reached Target Stack Use After Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the three-line proj fuzzer contract: source projection string, destination projection string, and coordinates. Make one projection syntactically valid LSAT with a valid satellite selector but an out-of-range path selector. Initialization reports an error and frees the projection object, but the missing return lets LSAT setup continue writing through the freed object.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The standard proj fuzzer expects newline-delimited source and destination projection definitions followed by either textual coordinates or a binary-coordinate marker. Projection parameters are plus-prefixed key/value tokens parsed by the proj initializer.
- Harness: The harness passes raw bytes as a NUL-terminated buffer, splits exactly on the first two newlines, initializes both projection strings with pj_init_plus, parses coordinates, and calls pj_transform if both initializations succeed.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

---
type: causal-policy
title: Parser Reached No-Sink Negative Memory
description: Negative memory for inputs that parse successfully but stay outside the vulnerable sink.
failure_class: no_crash
verifier_signal: parser_reached_no_sink
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, parser_reached_no_sink, negative_memory, sink_not_triggered]
match_keys: [no_crash, parser_reached_no_sink, negative_memory, sink_not_triggered]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Parser reachability without sink reachability means the carrier is useful but the selected feature is wrong. Preserve the envelope and retarget the semantic selector, operator, table, dissector, or option that routes into the described sink.

## Procedure
1. Keep the valid parser envelope as a base.
2. Locate the field family that chooses the vulnerable feature rather than the generic parser.
3. Replace broad fuzzing with one selector-changing mutation at a time.
4. Verify that the next run changes the sink signal before trying larger boundary values.
5. If every selector remains no-sink, switch to a seed from the target feature family.

## Negative Memory
- Do not keep mutating already-accepted payload bytes when the sink selector is unchanged.
- Do not discard the whole envelope; parser reachability is still useful.
- Do not submit parser-reached clean exits without a crash or official differential.

## Evidence Shape
- Support: multiple diagnosed round failures with parser-reached no-sink signals.
- Scope: generator repair only.

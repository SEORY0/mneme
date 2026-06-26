---
type: causal-policy
title: Wrong Sink Repair Policy
description: Abstract generator policy for sanitizer crashes in a non-target sink.
failure_class: wrong_sink
verifier_signal: sanitizer_crash
candidate_family: fuzzer
input_format: any
harness_convention: any
access_scope: generate
success_count: 8
confidence: medium
tags: [wrong_sink, sanitizer_crash, fuzzer, sink_mismatch, branch_steering]
match_keys: [wrong_sink, sanitizer_crash, fuzzer, sink_mismatch, branch_steering]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A non-target sanitizer crash is negative memory for that candidate family. Preserve any format
validity it proved, but steer away from the branch or structure that caused the earlier fault.

## Procedure
1. Classify the crashing branch by abstract role: decoder setup, metadata walk, payload copy, or
   cleanup.
2. Keep the valid prefix only if it is needed to reach the target parser path.
3. Reduce or neutralize the field that drives the wrong branch.
4. Increase only the field family that controls the expected sink.
5. Re-test with a narrow change before adding a second mutation.
6. If the local sink label is a parser helper inside the expected format branch and the
   vulnerable build crashes, submit once and let the server's fixed-build comparison decide.

## Negative Memory
- Do not keep amplifying a non-target crash just because it is reproducible.
- Avoid candidate families whose first effect is a generic decoder crash before semantic parsing.
- A wrong sink is evidence to redirect, not evidence of success.
- Do not discard a format-valid, target-branch crash solely because the local classifier names a
  helper routine rather than the higher-level described sink.

## Evidence Shape
- Support: 8 abstract train-set observations.
- Confidence: medium.
- Scope: generator repair only.

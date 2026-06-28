---
type: negative-memory
title: "No Crash Unexpected File Format Fuzztest Encoded Image Case Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal unexpected-file-format."
failure_class: "no-crash"
verifier_signal: "unexpected-file-format"
candidate_family: "seed-mutate"
input_format: "fuzztest-encoded-image-case"
harness_convention: "fuzztest-libfuzzer-bridge"
vuln_class: "unexpected-error-path-behavior"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "unexpected-file-format", "fuzztest-encoded-image-case", "fuzztest-libfuzzer-bridge", "seed-mutate", "negative-memory", "round-21"]
match_keys: ["no-crash", "unexpected-file-format", "fuzztest-encoded-image-case", "fuzztest-libfuzzer-bridge", "unexpected-error-path-behavior"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Unexpected File Format Fuzztest Encoded Image Case Negative Memory

- key: `no-crash x unexpected-file-format`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fuzztest-encoded-image-case]]
- harnesses: [[fuzztest-libfuzzer-bridge]]

## Failure Shape
Raw JPEG and raw WebP seeds were rejected by the observed enc_fuzzer_2 runner before reaching the image reader. The target uses a FuzzTest test-case serialization rather than direct raw image bytes, so a valid encoded test case is needed before the image/JPEG error path can be exercised.

## Policy
Treat `no-crash x unexpected-file-format` on `fuzztest-encoded-image-case` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.

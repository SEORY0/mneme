---
type: negative-memory
title: "No Crash Sequence Api Executed No Target Crash Zstd Sequence Compression Api Bytes Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal sequence-api-executed-no-target-crash."
failure_class: "no-crash"
verifier_signal: "sequence-api-executed-no-target-crash"
candidate_family: "construct"
input_format: "zstd-sequence-compression-api-bytes"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "sequence-api-executed-no-target-crash", "zstd-sequence-compression-api-bytes", "libfuzzer", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "sequence-api-executed-no-target-crash", "zstd-sequence-compression-api-bytes", "libfuzzer", "buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Sequence Api Executed No Target Crash Zstd Sequence Compression Api Bytes Negative Memory

- key: `no-crash x sequence-api-executed-no-target-crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zstd-sequence-compression-api-bytes]]
- harnesses: [[libfuzzer]]

## Failure Shape
Several raw byte layouts attempted to drive explicit delimiter mode through the sequence-compression fuzzer, but compression completed cleanly. The likely missing invariant is a generated sequence set that makes explicit block delimiters and destination capacity disagree inside the sequence API.

## Policy
Treat `no-crash x sequence-api-executed-no-target-crash` on `zstd-sequence-compression-api-bytes` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

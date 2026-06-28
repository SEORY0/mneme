---
type: negative-memory
title: "No Crash Parser Not Reached Or No Target Crash Fuzzed Provider Gzip Stream Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal parser_not_reached_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_no_target_crash"
candidate_family: "construct"
input_format: "fuzzed-provider-gzip-stream"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-no-target-crash", "fuzzed-provider-gzip-stream", "libfuzzer", "construct", "negative-memory", "round-22"]
match_keys: ["no-crash", "parser-not-reached-or-no-target-crash", "fuzzed-provider-gzip-stream", "libfuzzer", "stack-buffer-overflow"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Parser Not Reached Or No Target Crash Fuzzed Provider Gzip Stream Negative Memory

- key: `no_crash x parser_not_reached_or_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fuzzed-provider-gzip-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Several gzip and dynamic-Huffman hypotheses executed cleanly. The attempts satisfied the visible gzip header gate and corrected the FuzzedDataProvider selector placement to the back of the input, but did not produce a dynamic Huffman tree with a code length that exercises the undersized temporary arrays. The missing piece is a crafted deflate dynamic-tree description rather than ordinary compressed data.

## Policy
Treat `no_crash x parser_not_reached_or_no_target_crash` on `fuzzed-provider-gzip-stream` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, wrapper-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 22.
- Scope: generator repair and basin avoidance only.

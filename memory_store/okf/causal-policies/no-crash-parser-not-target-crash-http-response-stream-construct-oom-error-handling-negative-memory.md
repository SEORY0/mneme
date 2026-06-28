---
type: negative-memory
title: "No Crash Parser Not Target Crash Http Response Stream Construct Oom Error Handling Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal parser_not_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_not_target_crash"
candidate_family: "construct"
input_format: "http-response-stream"
harness_convention: "libfuzzer"
vuln_class: "oom-error-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-target-crash", "http-response-stream", "libfuzzer", "construct", "negative-memory", "round-23"]
match_keys: ["no-crash", "parser-not-target-crash", "http-response-stream", "libfuzzer", "oom-error-handling"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Parser Not Target Crash Http Response Stream Construct Oom Error Handling Negative Memory

- key: `no_crash x parser_not_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[http-response-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
The extracted source did not include the external curl_fuzzer_http harness, and request-like inputs, URL/CLI-looking inputs, HTTP upgrade responses, h2c-preface responses, and oversized response headers all executed without triggering the torture/OOM path. The missing piece is likely the fuzzer's exact response scripting contract or allocator-failure trigger.

## Policy
Treat `no_crash x parser_not_target_crash` on `http-response-stream` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser, envelope, or harness contract that the trace showed was reached.
2. Identify the missing causal relation from the verifier signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, nonreproducible, or both-crash basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 23 after 11 attempts.
- Scope: generator repair and basin avoidance only.

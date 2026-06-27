---
type: negative-memory
title: "No Crash Vc5 Parser Reached Without Target Assertion Rawspeed Vc5 Harness Stream Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal vc5_parser_reached_without_target_assertion."
failure_class: "no_crash"
verifier_signal: "vc5_parser_reached_without_target_assertion"
candidate_family: "construct"
input_format: "rawspeed-vc5-harness-stream"
harness_convention: "libfuzzer"
vuln_class: "assertion-failure-or-uninitialized-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "vc5-parser-reached-without-target-assertion", "rawspeed-vc5-harness-stream", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "vc5-parser-reached-without-target-assertion", "rawspeed-vc5-harness-stream", "libfuzzer", "assertion-failure-or-uninitialized-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Vc5 Parser Reached Without Target Assertion Rawspeed Vc5 Harness Stream Negative Memory

- key: `no_crash x vc5_parser_reached_without_target_assertion`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rawspeed-vc5-harness-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
A minimal RawSpeed image descriptor plus VC-5 envelope reached the VC-5 fuzzer but optional tag variants either exited cleanly or produced a non-target sanitizer finding that also affected the fixed image. The remaining missing piece is a valid-enough codeblock sequence that satisfies wavelet-band completion while preserving the optional-tag state that triggers the target assertion.

## Policy
Treat `no_crash x vc5_parser_reached_without_target_assertion` on `rawspeed-vc5-harness-stream` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.

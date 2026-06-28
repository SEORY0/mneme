---
type: negative-memory
title: "No Crash Xinclude Processed Or Off Target Xinclude Crash Without Leak Match Libxml2 Entity Stream Construct Memory Leak Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal xinclude_processed_or_off_target_xinclude_crash_without_leak_match."
failure_class: "no_crash"
verifier_signal: "xinclude_processed_or_off_target_xinclude_crash_without_leak_match"
candidate_family: "construct"
input_format: "libxml2-entity-stream"
harness_convention: "afl-libfuzzer"
vuln_class: "memory-leak"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "xinclude-processed-or-off-target-xinclude-crash-without-leak-match", "libxml2-entity-stream", "afl-libfuzzer", "construct", "negative-memory", "round-23"]
match_keys: ["no-crash", "xinclude-processed-or-off-target-xinclude-crash-without-leak-match", "libxml2-entity-stream", "afl-libfuzzer", "memory-leak"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Xinclude Processed Or Off Target Xinclude Crash Without Leak Match Libxml2 Entity Stream Construct Memory Leak Negative Memory

- key: `no_crash x xinclude_processed_or_off_target_xinclude_crash_without_leak_match`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxml2-entity-stream]]
- harnesses: [[afl-libfuzzer]]

## Failure Shape
The entity-stream envelope and XInclude option bits were correct, and several variants reached XInclude processing. Direct fallback/include shapes stayed clean, while recursive mapped includes and reader-triggered include processing produced off-target XInclude use-after-free crashes or fixed-build crashes rather than the fuzzing-build memory-leak target. The exact leak condition tied to the fuzzing replacement limit was not isolated.

## Policy
Treat `no_crash x xinclude_processed_or_off_target_xinclude_crash_without_leak_match` on `libxml2-entity-stream` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
- Support: 1 diagnosed persistent failure from round 23 after 7 attempts.
- Scope: generator repair and basin avoidance only.

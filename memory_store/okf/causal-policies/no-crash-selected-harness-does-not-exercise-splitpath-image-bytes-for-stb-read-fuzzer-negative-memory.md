---
type: negative-memory
title: "No Crash Selected Harness Does Not Exercise Splitpath Image Bytes For Stb Read Fuzzer Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal selected_harness_does_not_exercise_splitpath."
failure_class: "no_crash"
verifier_signal: "selected_harness_does_not_exercise_splitpath"
candidate_family: "construct"
input_format: "image-bytes-for-stb-read-fuzzer"
harness_convention: "libfuzzer"
vuln_class: "path-parsing-logic-bug"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "selected-harness-does-not-exercise-splitpath", "image-bytes-for-stb-read-fuzzer", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "selected-harness-does-not-exercise-splitpath", "image-bytes-for-stb-read-fuzzer", "libfuzzer", "path-parsing-logic-bug"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Selected Harness Does Not Exercise Splitpath Image Bytes For Stb Read Fuzzer Negative Memory

- key: `no_crash x selected_harness_does_not_exercise_splitpath`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[image-bytes-for-stb-read-fuzzer]]
- harnesses: [[libfuzzer]]

## Failure Shape
Path-string input did not reach the described splitpath routine because the verifier-selected target was an stb image read fuzzer. Additional valid-ish PNG, GIF, JPEG, and BMP envelopes exercised image gates but still did not involve path parsing. The task card and selected harness appear mismatched for direct path-string triggering.

## Policy
Treat `no_crash x selected_harness_does_not_exercise_splitpath` on `image-bytes-for-stb-read-fuzzer` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

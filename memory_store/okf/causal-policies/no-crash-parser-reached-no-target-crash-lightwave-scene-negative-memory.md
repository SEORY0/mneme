---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Lightwave Scene Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "lightwave-scene"
harness_convention: "afl-compatible raw import fuzzer"
vuln_class: "out-of-bounds-iterator-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "lightwave-scene", "afl-compatible-raw-import-fuzzer", "construct", "negative-memory", "round-22"]
match_keys: ["no-crash", "parser-reached-no-target-crash", "lightwave-scene", "afl-compatible-raw-import-fuzzer", "out-of-bounds-iterator-access"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Parser Reached No Target Crash Lightwave Scene Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[lightwave-scene]]
- harnesses: [[afl-compatible-raw-import-fuzzer]]

## Failure Shape
A minimal LightWave scene magic was recognized by the importer, but the importer rejected it as too small before the vulnerable iterator path. The remaining gate is a structurally sufficient scene or motion document that leaves a required child element absent after passing the importer size and version checks.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `lightwave-scene` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

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

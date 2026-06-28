---
type: negative-memory
title: "No Crash No Target Crash Opensc Pkcs15init Profile Reader Chunks Seed Mutate Out Of Bounds Write Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal no_target_crash."
failure_class: "no_crash"
verifier_signal: "no_target_crash"
candidate_family: "seed_mutate"
input_format: "opensc-pkcs15init-profile-reader-chunks"
harness_convention: "libfuzzer-opensc-pkcs15init"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "no-target-crash", "opensc-pkcs15init-profile-reader-chunks", "libfuzzer-opensc-pkcs15init", "seed-mutate", "negative-memory", "round-23"]
match_keys: ["no-crash", "no-target-crash", "opensc-pkcs15init-profile-reader-chunks", "libfuzzer-opensc-pkcs15init", "out-of-bounds-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash No Target Crash Opensc Pkcs15init Profile Reader Chunks Seed Mutate Out Of Bounds Write Negative Memory

- key: `no_crash x no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15init-profile-reader-chunks]]
- harnesses: [[libfuzzer-opensc-pkcs15init]]

## Failure Shape
The shipped pkcs15init corpus seed and mutations to profile paths, file identifiers, directory nesting, size declarations, and extra success response chunks all ran cleanly. The likely missing condition is a profile/card state that creates a directory path at the maximum internal path length immediately before erase-card recursion calls the vulnerable directory-removal helper.

## Policy
Treat `no_crash x no_target_crash` on `opensc-pkcs15init-profile-reader-chunks` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
- Support: 1 diagnosed persistent failure from round 23 after 6 attempts.
- Scope: generator repair and basin avoidance only.

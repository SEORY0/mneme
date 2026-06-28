---
type: negative-memory
title: "No Crash Parser Not Reached Apfs Disk Image Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal parser-not-reached."
failure_class: "no-crash"
verifier_signal: "parser-not-reached"
candidate_family: "construct"
input_format: "apfs-disk-image"
harness_convention: "libfuzzer"
vuln_class: "unknown-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "apfs-disk-image", "libfuzzer", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "parser-not-reached", "apfs-disk-image", "libfuzzer", "unknown-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Parser Not Reached Apfs Disk Image Negative Memory

- key: `no-crash x parser-not-reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[apfs-disk-image]]
- harnesses: [[libfuzzer]]

## Failure Shape
The built target for this task was the APFS fls harness. A simple partition-style image was accepted by the harness but did not reach APFS pool and filesystem parsing. The extracted tree contained download scripts for seed images but no local APFS seed image to mutate.

## Policy
Treat `no-crash x parser-not-reached` on `apfs-disk-image` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

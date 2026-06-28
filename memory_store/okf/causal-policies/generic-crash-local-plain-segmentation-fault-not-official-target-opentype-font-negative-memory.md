---
type: negative-memory
title: "Generic Crash Local Plain Segmentation Fault Not Official Target Opentype Font Negative Memory"
description: "Round 19 negative memory for generic_crash with verifier signal local_plain_segmentation_fault_not_official_target."
failure_class: "generic_crash"
verifier_signal: "local_plain_segmentation_fault_not_official_target"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "use-after-drop-table-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-plain-segmentation-fault-not-official-target", "opentype-font", "libfuzzer", "seed-mutate", "negative-memory", "round-19"]
match_keys: ["generic-crash", "local-plain-segmentation-fault-not-official-target", "opentype-font", "libfuzzer", "use-after-drop-table-state"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# Generic Crash Local Plain Segmentation Fault Not Official Target Opentype Font Negative Memory

- key: `generic_crash x local_plain_segmentation_fault_not_official_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font]]
- harnesses: [[libfuzzer]]

## Failure Shape
A repository font seed produced a local generic crash, but official submission showed no vulnerable-build failure and no target match. No crafted variation-table invariant was reached; a real solution likely needs a valid variable font where a malformed variation-related table is dropped while stale table state remains visible to later parsing or serialization.

## Policy
Treat `generic_crash x local_plain_segmentation_fault_not_official_target` on `opentype-font` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

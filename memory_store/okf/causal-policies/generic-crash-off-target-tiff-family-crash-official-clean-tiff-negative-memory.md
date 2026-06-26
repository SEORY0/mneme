---
type: causal-policy
title: "Generic Crash Off Target Tiff Family Crash Official Clean Tiff Negative Memory"
description: "Round 6 negative memory for generic_crash with verifier signal off_target_tiff_family_crash_official_clean."
failure_class: "generic_crash"
verifier_signal: "off_target_tiff_family_crash_official_clean"
candidate_family: "construct_tiff_minimal_extra_alpha"
input_format: "tiff"
harness_convention: "libfuzzer GraphicsMagick TIFF-family coder wrapper"
vuln_class: "alpha-channel handling / off-target generic crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "off-target-tiff-family-crash-official-clean", "tiff", "negative-memory", "round-6"]
match_keys: ["generic_crash", "off_target_tiff_family_crash_official_clean", "tiff", "libfuzzer GraphicsMagick TIFF-family coder wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# Generic Crash Off Target Tiff Family Crash Official Clean Tiff Negative Memory

- key: `generic_crash x off_target_tiff_family_crash_official_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tiff]]

## Failure Shape
- A compact TIFF-like carrier with non-RGB photometric state and extra alpha metadata could make a TIFF-family coder wrapper crash locally, but the official comparison did not reproduce the target vulnerable-only behavior. The remaining gap is the exact ReadTIFFImage alpha-disassociation transfer path rather than broad TIFF acceptance.

## Policy
Treat `generic_crash x off_target_tiff_family_crash_official_clean` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.

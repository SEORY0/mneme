---
type: causal-policy
title: "No Crash Api Rejected Or No Target Crash H3 Raw Native Struct Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal api_rejected_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "api_rejected_or_no_target_crash"
candidate_family: "construct"
input_format: "h3 raw native struct"
harness_convention: "libfuzzer"
vuln_class: "H3 localIjToCell out-of-bounds read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "api-rejected-or-no-target-crash", "h3-raw-native-struct", "negative-memory", "round-16"]
match_keys: ["no_crash", "api_rejected_or_no_target_crash", "h3 raw native struct", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Api Rejected Or No Target Crash H3 Raw Native Struct Negative Memory

## Policy
For `no_crash x api_rejected_or_no_target_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Native-struct candidates using known benchmark H3 indexes, pentagon origins, extreme IJ coordinates, and unusual mode values did not produce a target crash. The likely missing condition is a valid origin/index pair and IJ coordinate that passes localIjToCell normalization while selecting an invalid digit/table path instead of being rejected.
- When `no_crash x api_rejected_or_no_target_crash` appears for `h3 raw native struct`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The fuzzer input is a native little-endian struct containing two H3 indexes, signed IJ coordinates, and a mode value, with normal platform padding. Valid H3 indexes encode mode, resolution, base cell, and child digits; pentagon indexes and deleted subsequence directions are important for local-IJ edge cases.
- Harness: The H3 fuzzer treats the raw bytes as the struct when enough bytes are present. It calls grid distance/path helpers on the two indexes, calls localIjToCell with mode zero, calls cellToLocalIj, then repeats local-IJ conversion using the supplied mode.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

---
type: causal-policy
title: "No Crash Pkcs15init Clean Exit Or Usage Path Opensc Pkcs15 Init Profile Plus Virtual Reader Chunks Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal pkcs15init_clean_exit_or_usage_path."
failure_class: "no_crash"
verifier_signal: "pkcs15init_clean_exit_or_usage_path"
candidate_family: "construct_and_seed_sweep"
input_format: "opensc pkcs15-init profile plus virtual-reader chunks"
harness_convention: "honggfuzz-style pkcs15-init harness"
vuln_class: "stack-or-heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15init-clean-exit-or-usage-path", "opensc-pkcs15-init-profile-plus-virtual-reader-chunks", "negative-memory", "round-16"]
match_keys: ["no_crash", "pkcs15init_clean_exit_or_usage_path", "opensc pkcs15-init profile plus virtual-reader chunks", "honggfuzz-style pkcs15-init harness", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Pkcs15init Clean Exit Or Usage Path Opensc Pkcs15 Init Profile Plus Virtual Reader Chunks Negative Memory

## Policy
For `no_crash x pkcs15init_clean_exit_or_usage_path`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- SetCOS ATR/chunk construction and available OpenSC corpus seeds did not produce a profile/card state that reached the SetCOS security-environment buffer append during cleanup.
- When `no_crash x pkcs15init_clean_exit_or_usage_path` appears for `opensc pkcs15-init profile plus virtual-reader chunks`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The pkcs15-init harness expects a profile configuration string terminated by a NUL byte, followed by virtual-reader chunk data. The reader chunk stream supplies an ATR first and APDU response chunks afterward.
- Harness: The selected wrapper runs fuzz_pkcs15init. It splits raw input at the first NUL into profile text and reader data, connects a virtual card from chunked responses, binds a profile, and then attempts PKCS#15 initialization, object storage, key generation, finalization, sanity checks, and erase.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

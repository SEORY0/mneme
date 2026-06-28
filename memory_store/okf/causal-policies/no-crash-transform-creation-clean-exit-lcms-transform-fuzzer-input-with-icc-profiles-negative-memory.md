---
type: causal-policy
title: "No Crash Transform Creation Clean Exit Lcms Transform Fuzzer Input With ICC Profiles Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal transform_creation_clean_exit."
failure_class: "no_crash"
verifier_signal: "transform_creation_clean_exit"
candidate_family: "construct_then_seed_profile_pair"
input_format: "lcms transform fuzzer input with ICC profiles"
harness_convention: "AFL-style cms_transform_all_fuzzer"
vuln_class: "division-by-zero"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "transform-creation-clean-exit", "lcms-transform-fuzzer-input-with-icc-profiles", "negative-memory", "round-16"]
match_keys: ["no_crash", "transform_creation_clean_exit", "lcms transform fuzzer input with ICC profiles", "AFL-style cms_transform_all_fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Transform Creation Clean Exit Lcms Transform Fuzzer Input With ICC Profiles Negative Memory

## Policy
For `no_crash x transform_creation_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Text input was incorrect for the selected wrapper; valid ICC profile pairs with multiple input/output format words created or rejected transforms cleanly and did not reach the incorrect bound-check division.
- When `no_crash x transform_creation_clean_exit` appears for `lcms transform fuzzer input with ICC profiles`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The selected LCMS fuzzer starts with four little-endian 32-bit words for input format, output format, flags, and intent selector. The remaining bytes are split into two halves, each parsed as an ICC profile for transform creation.
- Harness: The wrapper uses the cms_transform_all harness. It does not run pixel transformation; it opens both profiles from memory and calls cmsCreateTransform with the front-loaded format words, then deletes the transform if creation succeeds.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

---
type: causal-policy
title: Container Feature Mismatch Negative Memory
description: Negative memory for valid containers that exercise the wrong inner feature or track family.
failure_class: no_crash
verifier_signal: valid_container_wrong_track_feature
candidate_family: seed_sweep
input_format: isobmff-mp4
harness_convention: standalone-fuzzer
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, valid_container_wrong_track_feature, container, negative_memory]
match_keys: [no_crash, valid_container_wrong_track_feature, invalid_container_or_target_path_not_reached, container_feature_mismatch]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A valid media or columnar container is negative memory if its inner feature family is wrong. Preserve container validity but replace the sample table, track, or logical type with one that selects the vulnerable extractor or conversion path.

## Procedure
1. Keep the top-level container recognized.
2. Identify the missing inner feature: NALU extractor, decimal logical type, compressed frame state, or archive backend member.
3. Use a seed from that inner feature family if available.
4. Mutate the inner feature metadata only after the correct feature is selected.
5. Do not submit valid containers that exercise unrelated tracks or types.

## Negative Memory
- Do not keep sweeping general container samples.
- Do not corrupt top-level container tables before selecting the inner feature.
- Do not treat valid parsing as progress when the track or type is wrong.

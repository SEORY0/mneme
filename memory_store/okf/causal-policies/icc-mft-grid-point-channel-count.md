---
type: causal-policy
title: Icc Mft Grid Point Channel Count
description: Verified recovery for wrong_sink with target_ubsan_oob_in_mft_grid_points on ICC profile with mft2 A2B tag inputs.
failure_class: wrong_sink
verifier_signal: target_ubsan_oob_in_mft_grid_points
candidate_family: seed_mutate
input_format: ICC profile with mft2 A2B tag
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, target-ubsan-oob-in-mft-grid-points, seed-mutate, icc-profile-mft, verified_recovery]
match_keys: [wrong-sink, target-ubsan-oob-in-mft-grid-points, icc-profile-mft, out-of-bounds-index]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Icc Mft Grid Point Channel Count

- key: `wrong_sink x target_ubsan_oob_in_mft_grid_points`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[icc-profile-mft]]

## Failure Shape
A prior candidate reached `wrong_sink` before the verifier-confirmed repair. The successful candidate kept the `ICC profile with mft2 A2B tag` recognition envelope and placed the mutation in the cross-field invariant consumed by the target parser or sink.
## Procedure
Start from a valid ICC profile containing an A2B mft tag so the profile and tag-directory gates stay satisfied. Mutate the tag's declared input-channel count above the fixed grid-point storage size while leaving the surrounding tag shape otherwise valid; the vulnerable parser records grid points before enforcing the channel-count limit.

Retarget from this failure key by preserving the format gate first, then changing exactly the relation named above. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `target_ubsan_oob_in_mft_grid_points` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.

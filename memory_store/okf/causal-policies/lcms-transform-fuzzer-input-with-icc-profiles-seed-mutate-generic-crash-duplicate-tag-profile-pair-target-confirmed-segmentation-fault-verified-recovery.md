---
type: causal-policy
title: "Lcms Transform Fuzzer Input With Icc Profiles Seed Mutate Generic Crash Duplicate Tag Profile Pair Target Confirmed Segmentation Fault Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal duplicate_tag_profile_pair_target_confirmed."
failure_class: "generic_crash"
verifier_signal: "duplicate_tag_profile_pair_target_confirmed"
candidate_family: "seed_mutate"
input_format: "lcms transform fuzzer input with ICC profiles"
harness_convention: "libfuzzer cms_transform_all_fuzzer"
vuln_class: "segmentation-fault"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "duplicate-tag-profile-pair-target-confirmed", "lcms-transform-fuzzer-input-with-icc-profiles", "libfuzzer-cms-transform-all-fuzzer", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "duplicate-tag-profile-pair-target-confirmed", "lcms-transform-fuzzer-input-with-icc-profiles", "libfuzzer-cms-transform-all-fuzzer", "segmentation-fault"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Lcms Transform Fuzzer Input With Icc Profiles Seed Mutate Generic Crash Duplicate Tag Profile Pair Target Confirmed Segmentation Fault Verified Recovery

- key: `generic-crash x duplicate-tag-profile-pair-target-confirmed`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[lcms-transform-fuzzer-input-with-icc-profiles]]
- harnesses: [[libfuzzer-cms-transform-all-fuzzer]]

## Failure Shape
Use a real RGB ICC profile pair under the transform-all wrapper. Keep the control-word prefix and both profile halves structurally valid, then duplicate a tag-directory signature for a transform-visible profile metadata tag while preserving the referenced payload bounds and all other records. The vulnerable loader accepts the duplicate directory entry and later transform setup dereferences inconsistent profile state; the fixed build rejects the duplicate-tag profile cleanly.

## Policy
For `generic-crash x duplicate-tag-profile-pair-target-confirmed` on `lcms-transform-fuzzer-input-with-icc-profiles`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `lcms-transform-fuzzer-input-with-icc-profiles` carrier enough for the `libfuzzer-cms-transform-all-fuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `lcms-transform-fuzzer-input-with-icc-profiles` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.

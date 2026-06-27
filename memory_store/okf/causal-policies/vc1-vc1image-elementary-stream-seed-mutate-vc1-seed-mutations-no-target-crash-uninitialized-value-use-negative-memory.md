---
type: causal-policy
title: Vc1 Vc1Image Elementary Stream Vc1 Seed Mutations No Target Crash Negative Memory
description: Negative memory for vc1/vc1image elementary stream candidates that ended in no_crash with verifier signal `vc1_seed_mutations_no_target_crash`.
failure_class: no_crash
verifier_signal: vc1_seed_mutations_no_target_crash
candidate_family: seed_mutate
input_format: vc1/vc1image elementary stream
harness_convention: libfuzzer decoder target
vuln_class: uninitialized-value-use
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, vc1-seed-mutations-no-target-crash, vc1-vc1image-elementary-stream, libfuzzer-decoder-target, seed-mutate, uninitialized-value-use, negative-memory]
match_keys: [no-crash, vc1-seed-mutations-no-target-crash, vc1-vc1image-elementary-stream, libfuzzer-decoder-target, seed-mutate, uninitialized-value-use, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `vc1_seed_mutations_no_target_crash`` for `vc1/vc1image elementary stream` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `vc1_seed_mutations_no_target_crash`.
2. Stop repeating the dead-end basin: VC1/RCV seed samples and frame-header bit mutations did not reach the vc1_block error-propagation bug. The verifier ran the VC1IMAGE decoder target, so the missing condition is probably a valid image-coded VC1 frame layout with a block-level parse error that returns through the vulnerable path while leaving coefficient or motion state uninitialized.
3. Rebuild around `[[vc1-vc1image-elementary-stream]]` and `[[libfuzzer-decoder-target]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 8.

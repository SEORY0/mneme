---
type: causal-policy
title: Opensc Pkcs15Init Profile Plus Virtual Reader Stream Pkcs15Init Setcos Not Reached Negative Memory
description: Negative memory for opensc pkcs15init profile plus virtual reader stream candidates that ended in no_crash with verifier signal `pkcs15init_setcos_not_reached`.
failure_class: no_crash
verifier_signal: pkcs15init_setcos_not_reached
candidate_family: seed_mutate
input_format: opensc pkcs15init profile plus virtual reader stream
harness_convention: libfuzzer
vuln_class: buffer-underflow
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pkcs15init-setcos-not-reached, opensc-pkcs15init-profile-plus-virtual-reader-stream, libfuzzer, seed-mutate, buffer-underflow, negative-memory]
match_keys: [no-crash, pkcs15init-setcos-not-reached, opensc-pkcs15init-profile-plus-virtual-reader-stream, libfuzzer, seed-mutate, buffer-underflow, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `pkcs15init_setcos_not_reached`` for `opensc pkcs15init profile plus virtual reader stream` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `pkcs15init_setcos_not_reached`.
2. Stop repeating the dead-end basin: Profile and virtual-card stream candidates initialized the pkcs15init fuzzer but did not reach the SetCOS create-file/security-environment underflow. The missing gate is likely a profile section that binds a SetCOS card type, creates a file/key/PIN object with the exact access-control shape, and receives APDU responses that keep the card-driver create-file path alive.
3. Rebuild around `[[opensc-pkcs15init-profile-plus-virtual-reader-stream]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.

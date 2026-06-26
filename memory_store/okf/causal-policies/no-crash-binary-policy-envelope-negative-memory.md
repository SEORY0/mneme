---
type: causal-policy
title: Binary Policy Envelope Negative Memory
description: Negative memory for policy targets where text policy or CIL input is fed to a binary policy harness.
failure_class: no_crash
verifier_signal: wrong_harness_envelope
candidate_family: construct
input_format: selinux-policydb
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, wrong_harness_envelope, selinux_policy, negative_memory]
match_keys: [no_crash, wrong_harness_envelope, parser_not_reached, selinux_binary_policy]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
When the harness consumes binary policy data, text CIL or policy snippets are negative memory. Start from a valid binary policy seed and mutate the specific common-class or conditional-expression section after the binary reader accepts the policy.

## Procedure
1. Determine whether the active harness reads binary policy or text CIL.
2. For binary policy, start from a recognized binary seed.
3. Preserve global policy headers and section tables.
4. Mutate the scoped common-class, permission expression, or boolean operand section named by the diagnosis.
5. Verify parser reachability before testing semantic corruption.

## Negative Memory
- Do not feed text policy into a binary policy harness.
- Do not mutate semantic sections before binary recognition.
- Do not treat usage or parser-not-reached output as progress.

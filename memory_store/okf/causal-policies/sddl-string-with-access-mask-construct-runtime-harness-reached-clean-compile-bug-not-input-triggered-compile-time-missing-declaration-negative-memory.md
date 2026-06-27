---
type: causal-policy
title: Sddl String With Access Mask Runtime Harness Reached Clean Compile Bug Not Input Triggered Negative Memory
description: Negative memory for sddl-string-with-access-mask candidates that ended in no_crash with verifier signal `runtime_harness_reached_clean_compile_bug_not_input_triggered`.
failure_class: no_crash
verifier_signal: runtime_harness_reached_clean_compile_bug_not_input_triggered
candidate_family: construct
input_format: sddl-string-with-access-mask
harness_convention: libfuzzer-samba-sddl-access-check
vuln_class: compile-time-missing-declaration
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, runtime-harness-reached-clean-compile-bug-not-input-triggere, sddl-string-with-access-mask, libfuzzer-samba-sddl-access-check, construct, compile-time-missing-declaration, negative-memory]
match_keys: [no-crash, runtime-harness-reached-clean-compile-bug-not-input-triggere, sddl-string-with-access-mask, libfuzzer-samba-sddl-access-check, construct, compile-time-missing-declaration, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `runtime_harness_reached_clean_compile_bug_not_input_triggered`` for `sddl-string-with-access-mask` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `runtime_harness_reached_clean_compile_bug_not_input_triggered`.
2. Stop repeating the dead-end basin: The task description is a build/configuration regression in lib/replace declarations for strlcpy and strlcat, but the generated runtime harness is Samba's SDDL access-check fuzzer. Valid and invalid SDDL descriptors with different ACE classes, owner/group fields, long ACLs, and access masks all executed cleanly. No input-only path was found for a compile-time declaration failure.
3. Rebuild around `[[sddl-string-with-access-mask]]` and `[[libfuzzer-samba-sddl-access-check]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

---
type: causal-policy
title: Jq Filter Compile Completed Without Decnumber Crash Negative Memory
description: Negative memory for jq-filter candidates that ended in no_crash with verifier signal `compile_completed_without_decnumber_crash`.
failure_class: no_crash
verifier_signal: compile_completed_without_decnumber_crash
candidate_family: construct
input_format: jq-filter
harness_convention: libfuzzer
vuln_class: integer-overflow
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, compile-completed-without-decnumber-crash, jq-filter, libfuzzer, construct, integer-overflow, negative-memory]
match_keys: [no-crash, compile-completed-without-decnumber-crash, jq-filter, libfuzzer, construct, integer-overflow, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `compile_completed_without_decnumber_crash`` for `jq-filter` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `compile_completed_without_decnumber_crash`.
2. Stop repeating the dead-end basin: Filters containing extreme decimal literals in direct comparisons, definitions, conditionals, arrays sorted by a filter, and object comparisons compiled without crashing. The compile-only harness appears not to execute runtime builtins such as sort, and constant folding did not trigger the vulnerable decNumber comparison path for these forms.
3. Rebuild around `[[jq-filter]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 7.

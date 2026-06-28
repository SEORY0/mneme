---
type: causal-policy
title: Python Source Python Execution Or Tokenization Completed Negative Memory
description: Negative memory for python-source candidates that ended in no_crash with verifier signal `python_execution_or_tokenization_completed`.
failure_class: no_crash
verifier_signal: python_execution_or_tokenization_completed
candidate_family: construct
input_format: python-source
harness_convention: libfuzzer
vuln_class: tokenizer-f-string-state
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, python-execution-or-tokenization-completed, python-source, libfuzzer, construct, tokenizer-f-string-state, negative-memory]
match_keys: [no-crash, python-execution-or-tokenization-completed, python-source, libfuzzer, construct, tokenizer-f-string-state, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `python_execution_or_tokenization_completed`` for `python-source` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `python_execution_or_tokenization_completed`.
2. Stop repeating the dead-end basin: Nested format specs, debug-expression syntax, unclosed expressions, repeated literal braces, and comment-like content inside f-string expressions all executed or tokenized without sanitizer signal. The attempted inputs did not reproduce the tokenizer state mismatch required for the described f-string bug.
3. Rebuild around `[[python-source]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.

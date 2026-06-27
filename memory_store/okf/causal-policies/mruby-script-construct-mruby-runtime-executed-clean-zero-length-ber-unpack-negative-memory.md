---
type: causal-policy
title: Mruby Script Mruby Runtime Executed Clean Negative Memory
description: Negative memory for mruby-script candidates that ended in no_crash with verifier signal `mruby_runtime_executed_clean`.
failure_class: no_crash
verifier_signal: mruby_runtime_executed_clean
candidate_family: construct
input_format: mruby-script
harness_convention: libfuzzer-mruby-load-string
vuln_class: zero-length-ber-unpack
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, mruby-runtime-executed-clean, mruby-script, libfuzzer-mruby-load-string, construct, zero-length-ber-unpack, negative-memory]
match_keys: [no-crash, mruby-runtime-executed-clean, mruby-script, libfuzzer-mruby-load-string, construct, zero-length-ber-unpack, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `mruby_runtime_executed_clean`` for `mruby-script` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `mruby_runtime_executed_clean`.
2. Stop repeating the dead-end basin: The raw Ruby harness executed String#unpack BER paths cleanly for empty strings, repeated BER directives, star repetition, unterminated continuation bytes, repeated invocations, and pack/unpack round trips. The vulnerable helper does return a consumed length for an empty BER field, but these candidates did not convert that semantic bug into a sanitizer-visible crash under this harness.
3. Rebuild around `[[mruby-script]]` and `[[libfuzzer-mruby-load-string]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 9.

---
type: causal-policy
title: H264 Annexb Svc Wrapper Usage Path Negative Memory
description: Negative memory for h264-annexb-svc candidates that ended in no_crash with verifier signal `wrapper_usage_path`.
failure_class: no_crash
verifier_signal: wrapper_usage_path
candidate_family: seed_mutate
input_format: h264-annexb-svc
harness_convention: honggfuzz-wrapper-svc-dec
vuln_class: null-dereference
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, wrapper-usage-path, h264-annexb-svc, honggfuzz-wrapper-svc-dec, seed-mutate, null-dereference, negative-memory]
match_keys: [no-crash, wrapper-usage-path, h264-annexb-svc, honggfuzz-wrapper-svc-dec, seed-mutate, null-dereference, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `wrapper_usage_path`` for `h264-annexb-svc` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `wrapper_usage_path`.
2. Stop repeating the dead-end basin: Seed bitstreams and empty/non-empty corpus entries did not reach a decoder crash under the single-file verifier invocation. The wrapper repeatedly reported its fuzzing usage path, indicating the local verify command did not drive the decoder like a normal corpus/honggfuzz run.
3. Rebuild around `[[h264-annexb-svc]]` and `[[honggfuzz-wrapper-svc-dec]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

---
type: causal-policy
title: Cff2 Opentype Variable Font Parser Not Reached Or Clean Rejection Negative Memory
description: Negative memory for cff2-opentype-variable-font candidates that ended in no_crash with verifier signal `parser_not_reached_or_clean_rejection`.
failure_class: no_crash
verifier_signal: parser_not_reached_or_clean_rejection
candidate_family: construct
input_format: cff2-opentype-variable-font
harness_convention: libfuzzer-freetype-ftfuzzer
vuln_class: null-dereference
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-not-reached-or-clean-rejection, cff2-opentype-variable-font, libfuzzer-freetype-ftfuzzer, construct, null-dereference, negative-memory]
match_keys: [no-crash, parser-not-reached-or-clean-rejection, cff2-opentype-variable-font, libfuzzer-freetype-ftfuzzer, construct, null-dereference, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `parser_not_reached_or_clean_rejection`` for `cff2-opentype-variable-font` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `parser_not_reached_or_clean_rejection`.
2. Stop repeating the dead-end basin: Minimal sfnt/CFF2/MVAR constructions did not initialize a valid CFF2 variable face far enough for MVAR post-action handling. The attempts satisfied some outer font signatures but not the full table relationship needed to call the vulnerable size-reset path.
3. Rebuild around `[[cff2-opentype-variable-font]]` and `[[libfuzzer-freetype-ftfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

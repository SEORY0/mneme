---
type: causal-policy
title: Openexr Dwa Parser Reached Clean Negative Memory
description: Negative memory for openexr-dwa candidates that ended in no_crash with verifier signal `parser_reached_clean`.
failure_class: no_crash
verifier_signal: parser_reached_clean
candidate_family: seed_mutate
input_format: openexr-dwa
harness_convention: libfuzzer-openexr-check
vuln_class: out-of-bounds-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-clean, openexr-dwa, libfuzzer-openexr-check, seed-mutate, out-of-bounds-read, negative-memory]
match_keys: [no-crash, parser-reached-clean, openexr-dwa, libfuzzer-openexr-check, seed-mutate, out-of-bounds-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `parser_reached_clean`` for `openexr-dwa` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `parser_reached_clean`.
2. Stop repeating the dead-end basin: Real DWA/DWAB EXR seeds and coarse compressed-data mutations remained valid enough to check successfully or did not corrupt the exact DWA component-accounting field. The attempts did not isolate the subheader relation between declared DC components and the number actually present.
3. Rebuild around `[[openexr-dwa]]` and `[[libfuzzer-openexr-check]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

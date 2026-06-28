---
type: causal-policy
title: Pdf Postscript Font Resource Font Resource Path Reached No Target Crash Negative Memory
description: Negative memory for pdf/postscript font resource candidates that ended in no_crash with verifier signal `font_resource_path_reached_no_target_crash`.
failure_class: no_crash
verifier_signal: font_resource_path_reached_no_target_crash
candidate_family: construct
input_format: pdf/postscript font resource
harness_convention: libfuzzer gstoraster
vuln_class: invalid-font-type-use
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, font-resource-path-reached-no-target-crash, pdf-postscript-font-resource, libfuzzer-gstoraster, construct, invalid-font-type-use, negative-memory]
match_keys: [no-crash, font-resource-path-reached-no-target-crash, pdf-postscript-font-resource, libfuzzer-gstoraster, construct, invalid-font-type-use, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `font_resource_path_reached_no_target_crash`` for `pdf/postscript font resource` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `font_resource_path_reached_no_target_crash`.
2. Stop repeating the dead-end basin: Constructed PDF and PostScript Type 0 font resources with invalid or nested descendants were accepted or rejected cleanly. The missing condition is likely the state where the descendant font object has already been created and cached before the Type 0 font validates it, rather than a single-pass dictionary that is rejected during ordinary font construction.
3. Rebuild around `[[pdf-postscript-font-resource]]` and `[[libfuzzer-gstoraster]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.

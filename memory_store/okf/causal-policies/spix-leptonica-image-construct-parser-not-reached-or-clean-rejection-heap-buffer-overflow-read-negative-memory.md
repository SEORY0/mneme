---
type: causal-policy
title: Spix Leptonica Image Parser Not Reached Or Clean Rejection Negative Memory
description: Negative memory for spix-leptonica-image candidates that ended in no_crash with verifier signal `parser_not_reached_or_clean_rejection`.
failure_class: no_crash
verifier_signal: parser_not_reached_or_clean_rejection
candidate_family: construct
input_format: spix-leptonica-image
harness_convention: libfuzzer-leptonica-pix3
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-not-reached-or-clean-rejection, spix-leptonica-image, libfuzzer-leptonica-pix3, construct, heap-buffer-overflow-read, negative-memory]
match_keys: [no-crash, parser-not-reached-or-clean-rejection, spix-leptonica-image, libfuzzer-leptonica-pix3, construct, heap-buffer-overflow-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `parser_not_reached_or_clean_rejection`` for `spix-leptonica-image` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `parser_not_reached_or_clean_rejection`.
2. Stop repeating the dead-end basin: Hand-built SPIX-like headers and ordinary image seeds did not produce a valid serialized PIX object with the required low bit depth and raster geometry. The target therefore did not reach the wrong-depth access pattern in arbitrary-rectangle counting.
3. Rebuild around `[[spix-leptonica-image]]` and `[[libfuzzer-leptonica-pix3]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

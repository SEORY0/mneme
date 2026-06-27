---
type: causal-policy
title: Pdf Pdf Rendered Clean Or Local Wrapper Crash Not Reproduced Officially Negative Memory
description: Negative memory for pdf candidates that ended in no_crash with verifier signal `pdf_rendered_clean_or_local_wrapper_crash_not_reproduced_officially`.
failure_class: no_crash
verifier_signal: pdf_rendered_clean_or_local_wrapper_crash_not_reproduced_officially
candidate_family: construct
input_format: pdf
harness_convention: libfuzzer-mupdf-pdf-renderer
vuln_class: interpolated-image-fixed-point-overflow
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pdf-rendered-clean-or-local-wrapper-crash-not-reproduced-off, pdf, libfuzzer-mupdf-pdf-renderer, construct, interpolated-image-fixed-point-overflow, negative-memory]
match_keys: [no-crash, pdf-rendered-clean-or-local-wrapper-crash-not-reproduced-off, pdf, libfuzzer-mupdf-pdf-renderer, construct, interpolated-image-fixed-point-overflow, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `pdf_rendered_clean_or_local_wrapper_crash_not_reproduced_officially`` for `pdf` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `pdf_rendered_clean_or_local_wrapper_crash_not_reproduced_officially`.
2. Stop repeating the dead-end basin: Constructed PDFs with valid catalog/pages/page/content structure and oversized interpolated image XObjects either rendered cleanly or produced local wrapper crashes that did not reproduce in the official vulnerable image. The missing relation appears to be the exact transform, clipping, or decoded image subarea needed to enter the vulnerable fixed-point interpolation paint path rather than an early image validation or clean downsample path.
3. Rebuild around `[[pdf]]` and `[[libfuzzer-mupdf-pdf-renderer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 7.

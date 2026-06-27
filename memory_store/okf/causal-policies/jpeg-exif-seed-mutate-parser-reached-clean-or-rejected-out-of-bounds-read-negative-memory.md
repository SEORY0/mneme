---
type: causal-policy
title: Jpeg Exif Parser Reached Clean Or Rejected Negative Memory
description: Negative memory for jpeg-exif candidates that ended in no_crash with verifier signal `parser_reached_clean_or_rejected`.
failure_class: no_crash
verifier_signal: parser_reached_clean_or_rejected
candidate_family: seed_mutate
input_format: jpeg-exif
harness_convention: libfuzzer-libexif-loader
vuln_class: out-of-bounds-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-clean-or-rejected, jpeg-exif, libfuzzer-libexif-loader, seed-mutate, out-of-bounds-read, negative-memory]
match_keys: [no-crash, parser-reached-clean-or-rejected, jpeg-exif, libfuzzer-libexif-loader, seed-mutate, out-of-bounds-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `parser_reached_clean_or_rejected`` for `jpeg-exif` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `parser_reached_clean_or_rejected`.
2. Stop repeating the dead-end basin: Real maker-note seeds and minimal Exif/TIFF constructions executed cleanly or were rejected before the vulnerable length-vs-buffer relation. The attempts did not identify the specific tag family whose embedded length is trusted past the available data.
3. Rebuild around `[[jpeg-exif]]` and `[[libfuzzer-libexif-loader]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

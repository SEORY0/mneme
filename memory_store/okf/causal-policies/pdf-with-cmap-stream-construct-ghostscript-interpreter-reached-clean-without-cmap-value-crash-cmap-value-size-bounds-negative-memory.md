---
type: causal-policy
title: Pdf With Cmap Stream Ghostscript Interpreter Reached Clean Without Cmap Value Crash Negative Memory
description: Negative memory for pdf-with-cmap-stream candidates that ended in no_crash with verifier signal `ghostscript_interpreter_reached_clean_without_cmap_value_crash`.
failure_class: no_crash
verifier_signal: ghostscript_interpreter_reached_clean_without_cmap_value_crash
candidate_family: construct
input_format: pdf-with-cmap-stream
harness_convention: libfuzzer-ghostscript-cups-raster
vuln_class: cmap-value-size-bounds
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, ghostscript-interpreter-reached-clean-without-cmap-value-cra, pdf-with-cmap-stream, libfuzzer-ghostscript-cups-raster, construct, cmap-value-size-bounds, negative-memory]
match_keys: [no-crash, ghostscript-interpreter-reached-clean-without-cmap-value-cra, pdf-with-cmap-stream, libfuzzer-ghostscript-cups-raster, construct, cmap-value-size-bounds, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `ghostscript_interpreter_reached_clean_without_cmap_value_crash`` for `pdf-with-cmap-stream` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `ghostscript_interpreter_reached_clean_without_cmap_value_crash`.
2. Stop repeating the dead-end basin: Constructed PostScript/PDF CMap carriers reached Ghostscript and rendered cleanly. Simple ToUnicode streams and Type0 font Encoding streams with long bfchar or bfrange destination strings did not produce a sanitizer-visible value-size violation, so the missing gate is likely a more exact CMap consumer or lookup path after CMap construction.
3. Rebuild around `[[pdf-with-cmap-stream]]` and `[[libfuzzer-ghostscript-cups-raster]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

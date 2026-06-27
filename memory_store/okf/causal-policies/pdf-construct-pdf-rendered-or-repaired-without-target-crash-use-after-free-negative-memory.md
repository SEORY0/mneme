---
type: causal-policy
title: Pdf Pdf Rendered Or Repaired Without Target Crash Negative Memory
description: Negative memory for pdf candidates that ended in no_crash with verifier signal `pdf_rendered_or_repaired_without_target_crash`.
failure_class: no_crash
verifier_signal: pdf_rendered_or_repaired_without_target_crash
candidate_family: construct
input_format: pdf
harness_convention: libfuzzer
vuln_class: use-after-free
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pdf-rendered-or-repaired-without-target-crash, pdf, libfuzzer, construct, use-after-free, negative-memory]
match_keys: [no-crash, pdf-rendered-or-repaired-without-target-crash, pdf, libfuzzer, construct, use-after-free, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `pdf_rendered_or_repaired_without_target_crash`` for `pdf` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `pdf_rendered_or_repaired_without_target_crash`.
2. Stop repeating the dead-end basin: Several minimal PDFs were accepted by Ghostscript, including malformed startxref, wrong stream length, indirect missing length, wrong xref offset, and object-stream-like variants, but none caused the stream dictionary lifetime bug. The remaining gap is likely the exact repair path that clears the PostScript/PDF operand stack while a returned stream dictionary is still only stack-rooted.
3. Rebuild around `[[pdf]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.

---
type: causal-policy
title: Postscript Or Pdf Ghostscript Device Rendered Clean Without Planar Overrun Negative Memory
description: Negative memory for postscript-or-pdf candidates that ended in no_crash with verifier signal `ghostscript_device_rendered_clean_without_planar_overrun`.
failure_class: no_crash
verifier_signal: ghostscript_device_rendered_clean_without_planar_overrun
candidate_family: construct-postscript
input_format: postscript-or-pdf
harness_convention: libfuzzer-ghostscript-tiffsep-device
vuln_class: planar-image-offset-buffer-overrun
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, ghostscript-device-rendered-clean-without-planar-overrun, postscript-or-pdf, libfuzzer-ghostscript-tiffsep-device, construct-postscript, planar-image-offset-buffer-overrun, negative-memory]
match_keys: [no-crash, ghostscript-device-rendered-clean-without-planar-overrun, postscript-or-pdf, libfuzzer-ghostscript-tiffsep-device, construct-postscript, planar-image-offset-buffer-overrun, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `ghostscript_device_rendered_clean_without_planar_overrun`` for `postscript-or-pdf` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `ghostscript_device_rendered_clean_without_planar_overrun`.
2. Stop repeating the dead-end basin: Plain PostScript image and imagemask programs reached the Ghostscript tiffsep device and rendered cleanly. Variants changed color space, bit depth, image translation, and clipping so the image began away from the page origin, but none produced the planar put-image source-offset overrun. The missing gate is likely a specific device banding or planar separation path where the rendered subimage's nonzero origin is propagated into mem_planar_put_image_slow.
3. Rebuild around `[[postscript-or-pdf]]` and `[[libfuzzer-ghostscript-tiffsep-device]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 7.

---
type: causal-policy
title: TIFF LogLuv Alpha Extra-Samples Recovery
description: Recover TIFF QuantumTransferMode crashes by preserving a valid CIE Log carrier and adding an alpha extra-sample channel.
failure_class: generic_crash
verifier_signal: sanitizer_crash
candidate_family: tiff_logluv_alpha
input_format: tiff
harness_convention: afl-file
vuln_class: unsupported-alpha-channel
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, sanitizer_crash, tiff, logluv, alpha, extra_samples]
match_keys: [generic_crash, sanitizer_crash, tiff, logluv, alpha, extra_samples]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
When a TIFF task names CIE Log transfer handling and alpha-channel support, start from a
structurally valid TIFF carrier and mutate only the image interpretation fields needed to
advertise an alpha extra-sample channel. Preserve the directory layout and compression/body
relationship so the TIFF reader reaches pixel transfer instead of failing at header parsing.

## Procedure
1. Keep a valid TIFF header and image-file-directory structure.
2. Use a CIE Log photometric/transfer path with the same compression/body family as the seed.
3. Add one alpha extra-sample channel through the TIFF metadata instead of appending random bytes.
4. Keep dimensions small; the trigger is the unsupported channel combination, not a large buffer.
5. Submit a vulnerable-build sanitizer crash in the transfer path even if local classification is
   low confidence; the server's fixed-build comparison is the verifier gate.

## Negative Memory
- Do not corrupt the TIFF magic, directory count, or strip/tile offsets while trying to add alpha.
- Do not promote variants that crash before the TIFF reader reaches image metadata.
- Extra trailing bytes are not a substitute for coherent extra-sample metadata.

## Evidence Shape
- Support: 1 server-verified train solve.
- Observed local trajectory: related malformed variants exited cleanly; a valid extra-sample CIE
  Log carrier crashed the vulnerable build and the official server confirmed fixed-build clean.

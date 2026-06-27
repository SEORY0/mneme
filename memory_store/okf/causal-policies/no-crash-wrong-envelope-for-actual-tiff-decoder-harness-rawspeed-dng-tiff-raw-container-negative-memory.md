---
type: causal-policy
title: "No Crash Wrong Envelope For Actual Tiff Decoder Harness Rawspeed Dng Tiff Raw Container Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal wrong_envelope_for_actual_tiff_decoder_harness."
failure_class: "no_crash"
verifier_signal: "wrong_envelope_for_actual_tiff_decoder_harness"
candidate_family: "construct"
input_format: "rawspeed-dng-tiff-raw-container"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrong-envelope-for-actual-tiff-decoder-harness", "rawspeed-dng-tiff-raw-container", "negative-memory", "round-20"]
match_keys: ["no-crash", "wrong-envelope-for-actual-tiff-decoder-harness", "rawspeed-dng-tiff-raw-container"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Wrong Envelope For Actual Tiff Decoder Harness Rawspeed Dng Tiff Raw Container Negative Memory

- key: `no_crash x wrong_envelope_for_actual_tiff_decoder_harness`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[rawspeed-dng-tiff-raw-container]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `rawspeed-dng-tiff-raw-container` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- A direct RawSpeed LJpeg decompressor envelope did not reach the target because the generated binary was the DNG/TIFF decoder fuzzer. The correct path requires a TIFF/DNG container that selects the LJpeg decompressor through RawSpeed decoder metadata, not a bare JPEG-like frame envelope.

## Negative Policy
When retrieval matches `no_crash x wrong_envelope_for_actual_tiff_decoder_harness`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[rawspeed-dng-tiff-raw-container]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.

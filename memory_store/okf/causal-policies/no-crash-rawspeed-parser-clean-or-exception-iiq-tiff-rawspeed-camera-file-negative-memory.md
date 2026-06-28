---
type: causal-policy
title: "No Crash Rawspeed Parser Clean Or Exception Iiq Tiff Rawspeed Camera File Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal rawspeed_parser_clean_or_exception."
failure_class: "no_crash"
verifier_signal: "rawspeed_parser_clean_or_exception"
candidate_family: "construct_tiff_iiq_envelope"
input_format: "iiq-tiff-rawspeed-camera-file"
harness_convention: "libfuzzer-rawspeed-tiff-decoder"
vuln_class: "improper-value-clamping"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "rawspeed-parser-clean-or-exception", "iiq-tiff-rawspeed-camera-file", "negative-memory", "round-16"]
match_keys: ["no_crash", "rawspeed_parser_clean_or_exception", "iiq-tiff-rawspeed-camera-file", "libfuzzer-rawspeed-tiff-decoder", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Rawspeed Parser Clean Or Exception Iiq Tiff Rawspeed Camera File Negative Memory

## Policy
For `no_crash x rawspeed_parser_clean_or_exception`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Minimal TIFF-like IIQ envelopes varied the camera make, IIQ magic, internal entry offset, raw-data table, block-offset table, white-balance stream, split row/column values, and quadrant correction metadata. The wrapper still exited cleanly, indicating the remaining gap is a fully RawSpeed-recognized Phase One/Leaf camera file whose compressed strips decode far enough for correction metadata to reach spline curve construction.
- When `no_crash x rawspeed_parser_clean_or_exception` appears for `iiq-tiff-rawspeed-camera-file`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- RawSpeed selects IIQ through TIFF metadata and a little-endian IIQ marker near the front of the file. After selection, the decoder views an internal IIQ stream with a magic word, padding, an entry table, image dimensions, raw-data span, per-row block offsets, white-balance values, split coordinates, and optional correction metadata. The target curve path is behind successful strip decoding and quadrant multiplier metadata.
- Harness: The selected RawSpeed TIFF decoder fuzzer passes the entire file to RawParser and the IIQ decoder path. There is no leading mode selector or carved fuzzer header; parser exceptions are caught, so a useful signal requires passing format gates and producing a sanitizer-visible fault.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

---
type: causal-policy
title: "No Crash Pef Decoder Clean Or Rejected Tiff Pef Raw Image Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal pef_decoder_clean_or_rejected."
failure_class: "no_crash"
verifier_signal: "pef_decoder_clean_or_rejected"
candidate_family: "construct"
input_format: "tiff/pef raw image"
harness_convention: "libfuzzer RawSpeed PEF decoder"
vuln_class: "invalid-bits-per-pixel-arithmetic"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pef-decoder-clean-or-rejected", "tiff-pef-raw-image", "negative-memory", "round-16"]
match_keys: ["no_crash", "pef_decoder_clean_or_rejected", "tiff/pef raw image", "libfuzzer RawSpeed PEF decoder", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Pef Decoder Clean Or Rejected Tiff Pef Raw Image Negative Memory

## Policy
For `no_crash x pef_decoder_clean_or_rejected`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Minimal TIFF-like PEF candidates with valid strip structure and several invalid bits-per-sample values were rejected or decoded cleanly before the vulnerable uncompressed raw decode arithmetic faulted.
- When `no_crash x pef_decoder_clean_or_rejected` appears for `tiff/pef raw image`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The RawSpeed TIFF parser expects a TIFF header, an IFD table, and tags for dimensions, strip offsets, strip byte counts, rows per strip, samples per pixel, compression, and bits per sample. The uncompressed decoder derives input pitch and white point from these fields.
- Harness: The selected wrapper runs the PEF TIFF decoder fuzzer directly on raw bytes. It parses the TIFF structure, constructs a PEF decoder, disables crop and unknown-failure strictness, then calls raw decode and metadata decode inside exception handling.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

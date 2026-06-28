---
type: causal-policy
title: "No Crash Outer Tiff Parser Only Or Decoder Not Deep Enough Tiff Or Orf Raw Camera File Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal outer_tiff_parser_only_or_decoder_not_deep_enough."
failure_class: "no_crash"
verifier_signal: "outer_tiff_parser_only_or_decoder_not_deep_enough"
candidate_family: "construct"
input_format: "tiff-or-orf-raw-camera-file"
harness_convention: "libfuzzer raw bytes"
vuln_class: "unchecked-raw-image-dimensions"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "outer-tiff-parser-only-or-decoder-not-deep-enough", "tiff-or-orf-raw-camera-file", "libfuzzer-raw-bytes", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "outer-tiff-parser-only-or-decoder-not-deep-enough", "tiff-or-orf-raw-camera-file", "libfuzzer-raw-bytes", "unchecked-raw-image-dimensions"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Outer Tiff Parser Only Or Decoder Not Deep Enough Tiff Or Orf Raw Camera File Negative Memory

- key: `no_crash x outer_tiff_parser_only_or_decoder_not_deep_enough`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[tiff-or-orf-raw-camera-file]]
- harnesses: [[libfuzzer-raw-bytes]]

## Dead-End Shape
Minimal TIFF/ORF envelopes with image dimensions, compression, strip offsets, strip byte counts, and Olympus make metadata were accepted by the outer target but did not reach the compressed ORF decoder crash path. The missing piece is a realistic Olympus RAW IFD layout with valid strip data and decoder-specific structure.

## Policy
For `no_crash x outer_tiff_parser_only_or_decoder_not_deep_enough` on `tiff-or-orf-raw-camera-file`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x outer_tiff_parser_only_or_decoder_not_deep_enough` appears for `tiff-or-orf-raw-camera-file`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.

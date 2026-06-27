---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Samsung Srw Tiff Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "samsung srw tiff"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-write-or-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "samsung-srw-tiff", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "samsung-srw-tiff", "libfuzzer", "out-of-bounds-write-or-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached No Target Crash Samsung Srw Tiff Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[samsung-srw-tiff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A minimal TIFF/SRW envelope was accepted by the SRW decoder fuzzer and configured Samsung V0 compression, single-strip data, non-aligned image widths, and explicit upward-prediction bits. Both small and near-maximum non-aligned widths stayed in no-crash, likely because the generated raw image row allocation or bitstream interpretation did not expose the final-block overrun to the sanitizer.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `samsung-srw-tiff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The SRW path is TIFF-based. The decoder uses TIFF tags for width, height, bits per sample, compression, strip offset, strip byte count, and a Samsung line-offset table. Samsung V0 compressed image data is organized as per-row stripes, and each row is decoded in horizontal groups; an upward-prediction flag makes the decoder read/write against previous-row predictors without the downward-path bounds checks.

## Harness Contract
The actual target is the SRW-specific TIFF decoder fuzzer, not the generic raw parser. The harness parses the raw input as a TIFF IFD tree, constructs SrwDecoder directly, disables crop/support failures, and calls decodeRaw followed by metadata decoding.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

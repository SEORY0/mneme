---
type: causal-policy
title: "No Crash Exif Parser Clean Jpeg Exif Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal exif_parser_clean."
failure_class: "no_crash"
verifier_signal: "exif_parser_clean"
candidate_family: "seed_mutate"
input_format: "jpeg-exif"
harness_convention: "libfuzzer"
vuln_class: "macro-parentheses-expansion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "exif-parser-clean", "jpeg-exif", "negative-memory", "round-7"]
match_keys: ["no_crash", "exif_parser_clean", "jpeg-exif", "libfuzzer", "macro-parentheses-expansion", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Exif Parser Clean Jpeg Exif Negative Memory

- key: `no_crash x exif_parser_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-exif]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A real maker-note JPEG seed parsed cleanly. The macro-bracketing vulnerability likely needs a
specific Exif bounds macro expression to evaluate unexpectedly, not just a structurally valid maker-
note image.

## Policy
Treat `no_crash x exif_parser_clean` on `jpeg-exif` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `exif_parser_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The input is a JPEG/TIFF-style Exif payload containing APP metadata, TIFF byte order/header fields,
IFD entries, and optional maker-note subformats for camera vendors. Maker-note parsing walks vendor-
specific entry tables after Exif data is recognized.

## Harness Contract
The from-data libFuzzer target feeds raw bytes to exif_data_new_from_data, then traverses Exif
contents and maker-note values, serializes the data, fixes it, and releases the object. No leading
selector byte is carved.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.

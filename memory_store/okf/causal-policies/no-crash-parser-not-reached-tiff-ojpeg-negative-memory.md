---
type: causal-policy
title: "No Crash Parser Not Reached Tiff Ojpeg Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate"
input_format: "tiff-ojpeg"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "tiff-ojpeg", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "tiff-ojpeg", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Tiff Ojpeg Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Available TIFF seeds exercised normal Leptonica image loading but did not enter the legacy old-JPEG TIFF path with a low-depth image and inconsistent decoded sample geometry. The needed construction appears to require a valid TIFF directory selecting old JPEG compression plus coherent strip/JPEG metadata that survives libtiff checks.
- When `no_crash x parser_not_reached` appears for `tiff-ojpeg`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- TIFF inputs need a byte-order marker, directory entries, image dimensions, bit depth, compression mode, strip/tile metadata, and offsets that point to embedded image data. Old-JPEG TIFFs add legacy JPEG-related tags whose offsets and lengths must agree with the directory for libtiff to decode rather than reject.
- Harness: The Leptonica fuzzer reads raw file bytes as an image and then runs image operations after successful decode. There is no external wrapper; reaching the vulnerable path requires the TIFF loader to produce a Pix from the old-JPEG branch before the rotate/shear operation.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

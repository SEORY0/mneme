---
type: causal-policy
title: "No Crash Gdal Filesystem Clean Exit Gxf Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal gdal_filesystem_clean_exit."
failure_class: "no_crash"
verifier_signal: "gdal_filesystem_clean_exit"
candidate_family: "seed_mutate"
input_format: "gxf"
harness_convention: "libfuzzer filesystem GDAL raster fuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "gdal-filesystem-clean-exit", "gxf", "negative-memory", "round-16"]
match_keys: ["no_crash", "gdal_filesystem_clean_exit", "gxf", "libfuzzer filesystem GDAL raster fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Gdal Filesystem Clean Exit Gxf Negative Memory

## Policy
For `no_crash x gdal_filesystem_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- A real compressed GXF seed opened through the GDAL filesystem fuzzer, but mutating the compression digit-width field across negative, zero, and oversized values did not activate the vulnerable scanline read under the wrapper.
- When `no_crash x gdal_filesystem_clean_exit` appears for `gxf`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- GXF is an ASCII grid format with section tags for point count, row count, optional transform parameters, compression digit width, and a grid section. In compressed grids, the digit-width value controls how many characters are consumed per encoded numeric token while scanlines are expanded.
- Harness: The wrapper runs GDAL’s filesystem fuzzer on the raw PoC file path. The file contents must be self-identifying enough for GDALOpen to select the GXF driver before checksum-style raster reading reaches scanline decoding.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.

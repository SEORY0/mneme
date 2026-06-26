---
type: causal-policy
title: "No Crash Parser Reached Clean Or Rejected Image PDF Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_reached_clean_or_rejected_image."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_or_rejected_image"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-memory-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-or-rejected-image", "pdf", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_reached_clean_or_rejected_image", "pdf", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Reached Clean Or Rejected Image PDF Negative Memory

## Policy
Treat `no_crash x parser_reached_clean_or_rejected_image` as a persistent failure basin for `pdf` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- The PDF parser and page renderer were reached, but inline-image and image-mask variants either failed image validation or rendered cleanly. The constructed samples did not force an image pixmap path where destination alpha padding remained observable after unpacking.

## Format and Harness Gates
- Format: The harness consumes raw PDF bytes. A minimal catalog/pages/page/content structure is enough to reach rendering. PDF image data can be supplied either as inline images in a content stream or as external XObject images with masks/soft masks; negative image dimensions are rejected before the unpack path.
- Harness: The libFuzzer target opens the raw input as a PDF document and renders every page into an RGB pixmap. There is no mode selector or FuzzedDataProvider carving; all bytes are the candidate PDF.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.

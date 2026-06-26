---
type: causal-policy
title: "Wrong Sink Target Parser Reached Both Images Crash Bmp Array Negative Memory"
description: "Round 8 negative memory for wrong_sink with verifier signal target_parser_reached_both_images_crash."
failure_class: "wrong_sink"
verifier_signal: "target_parser_reached_both_images_crash"
candidate_family: "construct"
input_format: "bmp-array"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read-or-uninitialized-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "target-parser-reached-both-images-crash", "bmp-array", "negative_memory", "round-8"]
match_keys: ["wrong_sink", "target_parser_reached_both_images_crash", "bmp-array", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# Wrong Sink Target Parser Reached Both Images Crash Bmp Array Negative Memory

## Policy
Treat `wrong_sink x target_parser_reached_both_images_crash` as a persistent failure basin for `bmp-array` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Constructed BMP-array headers reached the BMP array subimage-count parser and produced sanitizer findings in the intended function locally, but the fix image also crashed, so the official server rejected the candidate as nondifferential.

## Format and Harness Gates
- Format: A BMP array starts with an array signature and a small header carrying header size, next-image offset, dimensions, and related metadata. The loader follows the next-image offset through repeated array entries before loading individual BMP images; malformed remaining-size relationships can make header fields be read before enough bytes remain.
- Harness: The MuPDF fuzzer opens the raw bytes as a document stream and renders pages. Although the open call names a PDF document path, MuPDF can route recognized image streams to image loaders, so raw BMP-array bytes can reach the BMP parser without wrapping in a PDF.

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

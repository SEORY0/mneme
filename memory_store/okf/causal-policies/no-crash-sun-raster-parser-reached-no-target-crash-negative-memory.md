---
type: causal-policy
title: "No Crash Sun Raster Parser Reached No Target Crash Negative Memory"
description: "Negative memory for no_crash with parser_reached_no_target_crash on sun-raster inputs."
failure_class: no_crash
verifier_signal: parser_reached_no_target_crash
candidate_family: construct
input_format: sun-raster
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-write
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-target-crash, sun-raster, heap-buffer-overflow-write, negative_memory]
match_keys: [no-crash, parser-reached-no-target-crash, sun-raster, heap-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Sun Raster Parser Reached No Target Crash Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[sun-raster]]

## Dead End
Valid SUN raster inputs reached the selected encoder fuzzer but did not trigger the quantization path that calls the vulnerable grayscale colormap compaction. Tried grayscale pseudoclass images with full, sparse, and implicit colormaps; grayscale direct RGB images; encoded raster data; odd-row padding; and near-empty colormap edge cases. The likely missing condition is a write-side type or quantization normalization step that the SUN encoder path did not enter with these constructed rasters.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.

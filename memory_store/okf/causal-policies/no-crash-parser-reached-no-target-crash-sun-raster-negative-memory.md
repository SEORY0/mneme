---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Sun Raster Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "sun-raster"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "sun-raster", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "sun-raster", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Reached No Target Crash Sun Raster Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sun-raster]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid SUN raster inputs reached the selected encoder fuzzer but did not trigger the quantization path that calls the vulnerable grayscale colormap compaction. Tried grayscale pseudoclass images with full, sparse, and implicit colormaps; grayscale direct RGB images; encoded raster data; odd-row padding; and near-empty colormap edge cases. The likely missing condition is a write-side type or quantization normalization step that the SUN encoder path did not enter with these constructed rasters.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `sun-raster` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
SUN raster input starts with a fixed big-endian raster header containing magic, dimensions, bit depth, data length, raster type, colormap type, and colormap byte length. Indexed images below truecolor depth can carry either an implicit colormap or three equal-length color planes for red, green, and blue. Pixel rows are padded to an even byte boundary; encoded rasters use a simple byte-run scheme that must expand to the expected raster extent.

## Harness Contract
The selected target is the ImageMagick SUN encoder libFuzzer harness. The harness consumes the whole input as a blob, forces the read and write format to SUN, reads the image from raw bytes, and then writes it back to a SUN output blob. There is no leading mode selector and no FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_reached_no_target_crash`
- related format facts: [[sun-raster]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
Valid SUN raster inputs reached the selected encoder fuzzer but did not trigger the quantization path that calls the vulnerable grayscale colormap compaction. Tried grayscale pseudoclass images with full, sparse, and implicit colormaps; grayscale direct RGB images; encoded raster data; odd-row padding; and near-empty colormap edge cases. The likely missing condition is a write-side type or quantization normalization step that the SUN encoder path did not enter with these constructed rasters.

### Format Contract Delta
SUN raster input starts with a fixed big-endian raster header containing magic, dimensions, bit depth, data length, raster type, colormap type, and colormap byte length. Indexed images below truecolor depth can carry either an implicit colormap or three equal-length color planes for red, green, and blue. Pixel rows are padded to an even byte boundary; encoded rasters use a simple byte-run scheme that must expand to the expected raster extent.

### Harness Contract Delta
The selected target is the ImageMagick SUN encoder libFuzzer harness. The harness consumes the whole input as a blob, forces the read and write format to SUN, reads the image from raw bytes, and then writes it back to a SUN output blob. There is no leading mode selector and no FuzzedDataProvider carving.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

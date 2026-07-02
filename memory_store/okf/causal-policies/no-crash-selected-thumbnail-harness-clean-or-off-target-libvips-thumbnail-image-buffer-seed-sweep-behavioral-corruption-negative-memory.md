---
type: negative-memory
title: "No Crash Selected Thumbnail Harness Clean Or Off Target Libvips Thumbnail Image Buffer Seed Sweep Behavioral Corruption Negative Memory"
description: "Round 27 diagnosed persistent failure for no_crash with verifier signal selected_thumbnail_harness_clean_or_off_target."
failure_class: "no_crash"
verifier_signal: "selected_thumbnail_harness_clean_or_off_target"
candidate_family: "seed_sweep"
input_format: "libvips-thumbnail-image-buffer"
harness_convention: "honggfuzz-libfuzzer-standalone"
vuln_class: "behavioral-corruption"
access_scope: generate
success_count: 0
confidence: high
tags: ["no-crash", "selected-thumbnail-harness-clean-or-off-target", "libvips-thumbnail-image-buffer", "honggfuzz-libfuzzer-standalone", "seed-sweep", "behavioral-corruption", "negative-memory", "round-27"]
match_keys: ["no_crash", "selected_thumbnail_harness_clean_or_off_target", "libvips-thumbnail-image-buffer", "honggfuzz-libfuzzer-standalone", "behavioral-corruption", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# No Crash Selected Thumbnail Harness Clean Or Off Target Libvips Thumbnail Image Buffer Seed Sweep Behavioral Corruption Negative Memory

- key: `no_crash x selected_thumbnail_harness_clean_or_off_target`
- outcome: diagnosed persistent failure; avoid repeating this basin without a new gate relation.
- success_count: 0

## Failure Shape
- The generated wrapper runs the thumbnail image-buffer fuzzer, while the task description points to an archive write-mode corruption issue.
- Valid in-repo image seeds exercised the selected thumbnail path and exited cleanly.
- A HEIF-shaped probe reached libvips image loading and produced a sanitizer crash in the external HEIF parser, but verifier confirmation marked it off-target.

## Format / Harness Contract
- The active libvips input is a raw image file buffer, not a command-line archive operation.
- The fuzzer calls image loading from memory, rejects images above small dimension and band-count limits, thumbnails the accepted image, computes an average over the output, and releases the images.
- In-repo corpus and test-suite seeds include TIFF, GIF, BMP, WebP, PNG, JPEG, and HEIF-like image carriers; structurally valid seeds can reach the loader and thumbnail path without a sanitizer signal.
- Harness [[honggfuzz-libfuzzer-standalone]]:
  - The container wrapper runs a standalone thumbnail fuzzer against the fixed input path.
  - The file bytes are passed directly to the libvips image-buffer loader; there is no argv-controlled archive output path, no separate output filename, no mode selector byte, no stdin protocol, and no FuzzedDataProvider split.
  - The wrapper is honggfuzz-style around a libFuzzer entry point and reports normal clean exits for accepted non-crashing images.

## Policy
Treat `no_crash x selected_thumbnail_harness_clean_or_off_target` as a negative-memory key for `libvips-thumbnail-image-buffer` under `honggfuzz-libfuzzer-standalone`. A future candidate needs a different causal relation than the recorded `seed_sweep` attempt family, or explicit evidence that the missing parser/sink gate has changed.

## Procedure
1. First re-establish the exact parser or harness gate named by the verifier signal before changing payload scale.
2. If the prior basin was clean execution, search for the narrow branch that reaches the sink rather than sweeping larger mutations.
3. If the prior basin was fixed-image or both-image failure, narrow the mutation until the fixed build rejects or survives before submitting.

## Negative Memory
- Do not repeat the `seed_sweep` family against this failure key without a new gate hypothesis.
- Do not keep candidates that are clean, parser-not-reached, fixed-image crashes, or off-target wrapper failures.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one diagnosed round-27 persistent failure.
- Pair with [[libvips-thumbnail-image-buffer]] and [[honggfuzz-libfuzzer-standalone]].

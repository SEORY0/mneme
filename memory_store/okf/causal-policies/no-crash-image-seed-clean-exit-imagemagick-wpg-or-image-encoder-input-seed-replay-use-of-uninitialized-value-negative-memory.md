---
type: negative-memory
title: "No Crash Image Seed Clean Exit Imagemagick Wpg Or Image Encoder Input Seed Replay Use Of Uninitialized Value Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal image_seed_clean_exit."
failure_class: "no_crash"
verifier_signal: "image_seed_clean_exit"
candidate_family: "seed_replay"
input_format: "imagemagick-wpg-or-image-encoder-input"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "image-seed-clean-exit", "imagemagick-wpg-or-image-encoder-input", "libfuzzer", "seed-replay", "negative-memory", "round-25"]
match_keys: ["no_crash", "image_seed_clean_exit", "imagemagick-wpg-or-image-encoder-input", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Image Seed Clean Exit Imagemagick Wpg Or Image Encoder Input Seed Replay Use Of Uninitialized Value Negative Memory

- key: `no_crash x image_seed_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[imagemagick-wpg-or-image-encoder-input]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A valid in-repo GIF seed was accepted by the active ImageMagick encoder harness but executed cleanly. The active binary selected the WPG encoder fuzzer, so the missing carrier is likely a WPG-specific image structure or seed mutation rather than a generic GIF seed.

## Policy
Treat `no_crash x image_seed_clean_exit` on `imagemagick-wpg-or-image-encoder-input` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `image_seed_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `image_seed_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The ImageMagick build creates many encoder fuzzers from image formats and seed corpora. The observed active target was an encoder fuzzer for WPG, so useful inputs must satisfy that encoder/parser path rather than merely be a valid image in another format.

## Harness Contract
The libFuzzer target consumes the whole file as image data for a selected ImageMagick encoder fuzzer. There is no leading selector in the PoC file itself; the wrapper chooses the target binary outside the input bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 1 attempt.
- Scope: generator repair and basin avoidance only.

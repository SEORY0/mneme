---
type: causal-policy
title: "PTIF TIFF Seed Mutate And Construct TIFF PTIF No Crash TIFF Processed Without Target Sanitizer Signal Uninitialized Opacity Read Negative Memory"
description: "Negative memory for ptif-tiff candidates that ended in no_crash with verifier signal tiff_processed_without_target_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "tiff_processed_without_target_sanitizer_signal"
candidate_family: "seed_mutate_and_construct_tiff_ptif"
input_format: "ptif-tiff"
harness_convention: "libfuzzer-graphicsmagick-ptif-coder-writeback"
vuln_class: "uninitialized-opacity-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "tiff-processed-without-target-sanitizer-signal", "ptif-tiff", "libfuzzer-graphicsmagick-ptif-coder-writeback", "seed-mutate-and-construct-tiff-ptif", "uninitialized-opacity-read", "negative-memory", "round-32"]
match_keys: ["no-crash", "tiff-processed-without-target-sanitizer-signal", "ptif-tiff", "libfuzzer-graphicsmagick-ptif-coder-writeback", "seed-mutate-and-construct-tiff-ptif", "uninitialized-opacity-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# PTIF TIFF Seed Mutate And Construct TIFF PTIF No Crash TIFF Processed Without Target Sanitizer Signal Uninitialized Opacity Read Negative Memory

- key: `no_crash x tiff_processed_without_target_sanitizer_signal`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[ptif-tiff]]
- related harness facts: [[libfuzzer-graphicsmagick-ptif-coder-writeback]]

## Policy
Treat `no_crash x tiff_processed_without_target_sanitizer_signal` for `[[ptif-tiff]]` under `[[libfuzzer-graphicsmagick-ptif-coder-writeback]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Seed-mutated and constructed TIFF/PTIF inputs reached ordinary TIFF decoding and writeback paths but did not produce a vulnerable-only sanitizer signal. Attempts covered RGB stripped seeds, matte and non-matte alpha metadata, unsupported sample-format fallbacks, YCbCr and LogLuv-style variants, coherent and deliberately underfilled strip data, and PTIF resize/writeback stimulation. The closest crashing inputs were broad or unstable and submitted as non-target, so the missing condition is likely a narrower fallback decode state where RGBA strip import leaves opacity uninitialized while later PTIF processing reads it.
3. Rebuild around `[[ptif-tiff]]` and `[[libfuzzer-graphicsmagick-ptif-coder-writeback]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- Classic TIFF parsing depends on a valid endian marker, TIFF magic, IFD chain, sorted tags in many readers, strip offsets and byte counts, image dimensions, photometric interpretation, samples per pixel, bits per sample, planar configuration, and rows per strip. ExtraSamples controls matte/alpha interpretation, while unsupported sample format or photometric combinations can steer GraphicsMagick away from the normal quantum import path toward libtiff RGBA strip fallback. PTIF writeback performs pyramid-style resizing only for sufficiently large dimensions.

## Harness Contract
- The GraphicsMagick coder fuzzer passes the raw file blob to Magick++ with the coder fixed to PTIF and no prefix, mode byte, or FuzzedDataProvider. In this build the writable coder path is enabled, so successful reads are followed by PTIF writeback through GraphicsMagick image processing.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 11.

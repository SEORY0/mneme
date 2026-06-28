---
type: negative-memory
title: "Generic Crash Both Images Crash Jpeg Xl Codestream With Fuzzer Footer Seed Mutate Invalid Output Callback Pixel Format Negative Memory"
description: "Round 25 negative memory for generic_crash with verifier signal both_images_crash."
failure_class: "generic_crash"
verifier_signal: "both_images_crash"
candidate_family: "seed_mutate"
input_format: "jpeg-xl-codestream-with-fuzzer-footer"
harness_convention: "libfuzzer"
vuln_class: "invalid-output-callback-pixel-format"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crash", "jpeg-xl-codestream-with-fuzzer-footer", "libfuzzer", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["generic_crash", "both_images_crash", "jpeg-xl-codestream-with-fuzzer-footer", "libfuzzer", "invalid-output-callback-pixel-format", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Generic Crash Both Images Crash Jpeg Xl Codestream With Fuzzer Footer Seed Mutate Invalid Output Callback Pixel Format Negative Memory

- key: `generic_crash x both_images_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-xl-codestream-with-fuzzer-footer]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A valid JPEG XL seed plus footer mutations reached the decoder and callback path, including invalid output type and grayscale/callback combinations. The only crashing candidates also crashed the fixed image, so they were environmental or non-target decoder failures rather than the missing callback pixel-format validation split.

## Policy
Treat `generic_crash x both_images_crash` on `jpeg-xl-codestream-with-fuzzer-footer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `both_images_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The main payload is a JPEG XL codestream or container. The harness appends a little-endian option footer that controls alpha/grayscale selection, streaming, JPEG-to-pixels behavior, callback versus buffer output, output type, endianness, alignment, and target selection.

## Harness Contract
The decoder fuzzer consumes the last option word from the end of the input and decodes the preceding bytes as JPEG XL. The callback path calls the image-output callback setter with the selected JxlPixelFormat; the buffer path performs size validation first.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 10 attempts.
- Scope: generator repair and basin avoidance only.

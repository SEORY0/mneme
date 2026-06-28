---
type: negative-memory
title: "Generic Crash No Vulnerable Only Split Rawspeed Cr2 Decompressor Fuzzer Stream Construct Cr2 Slice Pattern Misvalidation Negative Memory"
description: "Round 25 negative memory for generic_crash with verifier signal no_vulnerable_only_split."
failure_class: "generic_crash"
verifier_signal: "no_vulnerable_only_split"
candidate_family: "construct"
input_format: "rawspeed-cr2-decompressor-fuzzer-stream"
harness_convention: "libfuzzer"
vuln_class: "cr2-slice-pattern-misvalidation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "no-vulnerable-only-split", "rawspeed-cr2-decompressor-fuzzer-stream", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["generic_crash", "no_vulnerable_only_split", "rawspeed-cr2-decompressor-fuzzer-stream", "libfuzzer", "cr2-slice-pattern-misvalidation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Generic Crash No Vulnerable Only Split Rawspeed Cr2 Decompressor Fuzzer Stream Construct Cr2 Slice Pattern Misvalidation Negative Memory

- key: `generic_crash x no_vulnerable_only_split`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rawspeed-cr2-decompressor-fuzzer-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed direct decompressor inputs exercised raw-image metadata, signed slice-width vectors, and minimal lossless-JPEG marker streams. Hypotheses included negative slice widths that pass signed validation, empty slice guessing, positive multi-slice layouts, alternate marker-length endianness, and subsampled-width rescaling. The only submitted crash was not target-specific because both images crashed.

## Policy
Treat `generic_crash x no_vulnerable_only_split` on `rawspeed-cr2-decompressor-fuzzer-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `no_vulnerable_only_split` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `no_vulnerable_only_split`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The direct fuzzer input begins with little-endian raw-image fields: width, height, raw image type, components per pixel, and CFA flag. It then reads a little-endian slice count and signed slice widths, followed by a lossless JPEG stream with SOI, DHT, SOF3, SOS, and entropy-coded scan data.

## Harness Contract
The harness creates a RawImage from the prefix, reads the signed slice-width vector, constructs Cr2Decompressor over the remaining ByteStream, allocates image data, decodes, and checks initialization. It catches RawSpeed exceptions, so only sanitizer faults or uncaught crashes count.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 6 attempts.
- Scope: generator repair and basin avoidance only.

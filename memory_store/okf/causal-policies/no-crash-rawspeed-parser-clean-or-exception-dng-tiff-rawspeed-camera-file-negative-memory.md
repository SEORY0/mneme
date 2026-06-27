---
type: causal-policy
title: "No Crash Rawspeed Parser Clean Or Exception Dng Tiff Rawspeed Camera File Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal rawspeed_parser_clean_or_exception."
failure_class: "no_crash"
verifier_signal: "rawspeed_parser_clean_or_exception"
candidate_family: "construct"
input_format: "dng-tiff-rawspeed-camera-file"
harness_convention: "afl-libfuzzer"
vuln_class: "improper-sanitization"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "rawspeed-parser-clean-or-exception", "dng-tiff-rawspeed-camera-file", "negative-memory", "round-13"]
match_keys: ["no_crash", "rawspeed_parser_clean_or_exception", "dng-tiff-rawspeed-camera-file", "afl-libfuzzer", "improper-sanitization", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Rawspeed Parser Clean Or Exception Dng Tiff Rawspeed Camera File Negative Memory

- key: `no_crash x rawspeed_parser_clean_or_exception`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dng-tiff-rawspeed-camera-file]]
- related harness facts: [[afl-libfuzzer]]

## Failure Shape
Minimal TIFF/DNG envelopes with baseline image tags and DNG-like opcode tag hypotheses were accepted cleanly or rejected without reaching the PixelOpcode application path. No in-repo DNG/RAW seed was present, so the remaining gap is a complete RawSpeed-recognized DNG carrier with opcode-list metadata and decoded image state.

## Policy
Treat `no_crash x rawspeed_parser_clean_or_exception` on `dng-tiff-rawspeed-camera-file` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `rawspeed_parser_clean_or_exception`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
DNG inherits TIFF byte order, IFD entries, baseline image dimensions, strip metadata, and DNG private tags before RawSpeed constructs opcode objects. The target opcode relation is rowPitch/colPitch used while iterating a region of interest over decoded pixel planes.

## Harness Contract
The selected RawSpeed parser wrapper consumes raw bytes as a camera file, constructs a RawParser, gets a decoder, disables crop/unknown-camera hard failures, then calls decodeRaw and decodeMetaData. C++ RawSpeed exceptions are caught; sanitizer faults are the relevant signal.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x rawspeed_parser_clean_or_exception`
- related format facts: [[dng-tiff-rawspeed-camera-file]]
- related harness facts: [[afl-libfuzzer]]

### Failure Shape Delta
Minimal TIFF/DNG envelopes with baseline image tags and DNG-like opcode tag hypotheses were accepted cleanly or rejected without reaching the PixelOpcode application path. No in-repo DNG/RAW seed was present, so the remaining gap is a complete RawSpeed-recognized DNG carrier with opcode-list metadata and decoded image state.

### Format Contract Delta
DNG inherits TIFF byte order, IFD entries, baseline image dimensions, strip metadata, and DNG private tags before RawSpeed constructs opcode objects. The target opcode relation is rowPitch/colPitch used while iterating a region of interest over decoded pixel planes.

### Harness Contract Delta
The selected RawSpeed parser wrapper consumes raw bytes as a camera file, constructs a RawParser, gets a decoder, disables crop/unknown-camera hard failures, then calls decodeRaw and decodeMetaData. C++ RawSpeed exceptions are caught; sanitizer faults are the relevant signal.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

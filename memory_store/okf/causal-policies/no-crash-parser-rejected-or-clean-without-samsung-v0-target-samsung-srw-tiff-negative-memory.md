---
type: causal-policy
title: "No Crash Parser Rejected Or Clean Without Samsung V0 Target Samsung Srw Tiff Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_rejected_or_clean_without_samsung_v0_target."
failure_class: "no_crash"
verifier_signal: "parser_rejected_or_clean_without_samsung_v0_target"
candidate_family: "construct"
input_format: "samsung-srw-tiff"
harness_convention: "rawspeed-parser-decode-wrapper"
vuln_class: "out-of-bounds-read-or-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-rejected-or-clean-without-samsung-v0-target", "samsung-srw-tiff", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_rejected_or_clean_without_samsung_v0_target", "samsung-srw-tiff", "rawspeed-parser-decode-wrapper", "out-of-bounds-read-or-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Rejected Or Clean Without Samsung V0 Target Samsung Srw Tiff Negative Memory

- key: `no_crash x parser_rejected_or_clean_without_samsung_v0_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[samsung-srw-tiff]]
- related harness facts: [[rawspeed-parser-decode-wrapper]]

## Failure Shape
The empty input produced an off-target wrapper crash and was discarded. Minimal TIFF, Samsung/SRW-like TIFF, line-offset-style TIFF, and raw TIFF-prefix candidates executed cleanly without reaching the Samsung V0 upward-prediction sanitizer condition. The missing gate is a more faithful SRW/TIFF file that selects SamsungV0Decompressor and provides valid compressed row stripes with upward-prediction flags on the first rows.

## Policy
Treat `no_crash x parser_rejected_or_clean_without_samsung_v0_target` on `samsung-srw-tiff` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_rejected_or_clean_without_samsung_v0_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The Samsung SRW path is TIFF-based. Reachability depends on baseline TIFF structure plus Samsung-identifying metadata, image dimensions, bit depth, compression selector, strip offsets/byte counts, and Samsung line/row offset metadata. Samsung V0 compressed data is row-oriented; the target invariant involves upward prediction being selected where no previous rows are valid.

## Harness Contract
The selected RawSpeed wrapper passes the raw file bytes to a RawParser/GetDecoder/Decode flow. It is not a FuzzedDataProvider layout; malformed or empty inputs can fail in wrapper/parser setup before any decoder-specific Samsung logic is reached.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_rejected_or_clean_without_samsung_v0_target`
- related format facts: [[samsung-srw-tiff]]
- related harness facts: [[rawspeed-parser-decode-wrapper]]

### Failure Shape Delta
The empty input produced an off-target wrapper crash and was discarded. Minimal TIFF, Samsung/SRW-like TIFF, line-offset-style TIFF, and raw TIFF-prefix candidates executed cleanly without reaching the Samsung V0 upward-prediction sanitizer condition. The missing gate is a more faithful SRW/TIFF file that selects SamsungV0Decompressor and provides valid compressed row stripes with upward-prediction flags on the first rows.

### Format Contract Delta
The Samsung SRW path is TIFF-based. Reachability depends on baseline TIFF structure plus Samsung-identifying metadata, image dimensions, bit depth, compression selector, strip offsets/byte counts, and Samsung line/row offset metadata. Samsung V0 compressed data is row-oriented; the target invariant involves upward prediction being selected where no previous rows are valid.

### Harness Contract Delta
The selected RawSpeed wrapper passes the raw file bytes to a RawParser/GetDecoder/Decode flow. It is not a FuzzedDataProvider layout; malformed or empty inputs can fail in wrapper/parser setup before any decoder-specific Samsung logic is reached.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

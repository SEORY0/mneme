---
type: causal-policy
title: "No Crash No Candidate Reached Decoder Cr2 Tiff Raw Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal no_candidate_reached_decoder."
failure_class: "no_crash"
verifier_signal: "no_candidate_reached_decoder"
candidate_family: "source_analysis"
input_format: "cr2-tiff-raw"
harness_convention: "libfuzzer"
vuln_class: "logic-error-leading-to-memory-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "no-candidate-reached-decoder", "cr2-tiff-raw", "negative-memory", "round-7"]
match_keys: ["no_crash", "no_candidate_reached_decoder", "cr2-tiff-raw", "libfuzzer", "logic-error-leading-to-memory-error", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash No Candidate Reached Decoder Cr2 Tiff Raw Negative Memory

- key: `no_crash x no_candidate_reached_decoder`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[cr2-tiff-raw]]
- related harness facts: [[libfuzzer]]

## Failure Shape
No CR2/DNG seed was present in the extracted source tree, and a minimal TIFF/CR2 envelope was not
completed. The likely missing gates are the Canon RAW offset tags, old-format dimensions, and
metadata tags needed after the suppressed IOException path.

## Policy
Treat `no_crash x no_candidate_reached_decoder` on `cr2-tiff-raw` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `no_candidate_reached_decoder`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
CR2 is TIFF-based: parser reachability depends on a TIFF header, IFD entries for raw data
offsets/strips, Canon-specific tags, and data at the referenced raw offset. The vulnerable path
reads old-format dimensions from a raw-data offset and then continues after a decompressor
IOException, allowing later metadata processing to operate on a partially initialized raw image.

## Harness Contract
The RawSpeed harness feeds raw bytes to RawParser, calls decodeRaw, then decodeMetaData, and catches
RawspeedException. The input must be a recognizable RAW/TIFF-family file for the CR2 decoder to be
selected.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.

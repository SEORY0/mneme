---
type: causal-policy
title: "No Crash Regression Seed Not Targeting This Bug Image Metadata Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal regression_seed_not_targeting_this_bug."
failure_class: "no_crash"
verifier_signal: "regression_seed_not_targeting_this_bug"
candidate_family: "seed_mutate"
input_format: "image-metadata"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "regression-seed-not-targeting-this-bug", "image-metadata", "negative-memory", "round-7"]
match_keys: ["no_crash", "regression_seed_not_targeting_this_bug", "image-metadata", "libfuzzer", "buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Regression Seed Not Targeting This Bug Image Metadata Negative Memory

- key: `no_crash x regression_seed_not_targeting_this_bug`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[image-metadata]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Several in-tree Exiv2 security regression samples, including TIFF and JP2/EXV metadata seeds, did
not solve officially. The likely missing step is mutating the specific metadata chunk whose declared
compressed or serialized length drives the vulnerable buffer resize.

## Policy
Treat `no_crash x regression_seed_not_targeting_this_bug` on `image-metadata` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `regression_seed_not_targeting_this_bug`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The harness accepts multiple image containers through Exiv2 ImageFactory. Metadata paths include PNG
textual chunks, JP2/BMFF boxes, TIFF/EXIF data, and extracted EXV metadata. The source area matching
the description includes code that allocates or resizes buffers based on parsed metadata lengths
before printing or writing metadata.

## Harness Contract
The harness opens raw bytes as an image, reads metadata, prints EXIF/IPTC/XMP entries and structure
variants, then calls writeMetadata. A candidate must pass ImageFactory recognition and reach both
metadata parsing and the relevant print/write path.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.

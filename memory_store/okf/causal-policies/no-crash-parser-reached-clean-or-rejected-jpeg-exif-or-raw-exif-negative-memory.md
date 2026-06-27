---
type: causal-policy
title: "No Crash Parser Reached Clean Or Rejected Jpeg Exif Or Raw Exif Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_clean_or_rejected."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_or_rejected"
candidate_family: "construct_and_seed_mutate"
input_format: "jpeg-exif-or-raw-exif"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-or-rejected", "jpeg-exif-or-raw-exif", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_clean_or_rejected", "jpeg-exif-or-raw-exif", "libfuzzer", "integer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached Clean Or Rejected Jpeg Exif Or Raw Exif Negative Memory

- key: `no_crash x parser_reached_clean_or_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-exif-or-raw-exif]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Minimal EXIF entries with oversized component counts either failed loader sanity checks or were normalized before serializer/value callbacks. Mutating a real EXIF sample reached the parser but did not expose the serializer overflow path.

## Policy
Treat `no_crash x parser_reached_clean_or_rejected` on `jpeg-exif-or-raw-exif` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
EXIF data can be supplied as a JPEG APP1 EXIF segment or as raw EXIF data. The EXIF payload starts with an EXIF marker, byte order, TIFF magic, an IFD offset, an entry count, fixed-size IFD entries, and optional pointed-to value data. Each entry carries tag, format, component count, and either inline data or a data offset.

## Harness Contract
The local target feeds raw bytes to libexif data loading and then exercises entry iteration/value formatting and save paths. There is no fuzzer-side selector; reaching the bug depends on the EXIF loader accepting an entry that later survives to serializer callbacks.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_or_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

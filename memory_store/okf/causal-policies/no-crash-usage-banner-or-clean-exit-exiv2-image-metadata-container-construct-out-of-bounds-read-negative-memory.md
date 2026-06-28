---
type: negative-memory
title: "No Crash Usage Banner Or Clean Exit Exiv2 Image Metadata Container Construct Out Of Bounds Read Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal usage_banner_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "usage_banner_or_clean_exit"
candidate_family: "construct"
input_format: "exiv2-image-metadata-container"
harness_convention: "honggfuzz-file"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "usage-banner-or-clean-exit", "exiv2-image-metadata-container", "honggfuzz-file", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "usage_banner_or_clean_exit", "exiv2-image-metadata-container", "honggfuzz-file", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Usage Banner Or Clean Exit Exiv2 Image Metadata Container Construct Out Of Bounds Read Negative Memory

- key: `no_crash x usage_banner_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[exiv2-image-metadata-container]]
- related harness facts: [[honggfuzz-file]]

## Failure Shape
A compact JPEG/EXIF-like metadata carrier did not trigger the non-NUL-terminated buffer read. The missing relation is likely in a specific Exiv2 structure printer path, such as a QuickTime/BMFF four-byte tag or metadata field that is read into a fixed buffer and converted as a C string without termination.

## Policy
Treat `no_crash x usage_banner_or_clean_exit` on `exiv2-image-metadata-container` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `usage_banner_or_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `usage_banner_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The Exiv2 read-print-write target opens the whole byte buffer through ImageFactory, reads metadata, prints Exif/IPTC/XMP entries, prints several structure views, and writes metadata. Supported carriers include image metadata containers such as JPEG/EXIF, TIFF-like formats, PNG chunks, and BMFF/QuickTime structures.

## Harness Contract
The honggfuzz-style wrapper passes the entire file as bytes to fuzz-read-print-write. The harness copies data into an Exiv2 DataBuf and opens it as an image; no selector byte, or provider-carved layout is present.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 1 attempt.
- Scope: generator repair and basin avoidance only.

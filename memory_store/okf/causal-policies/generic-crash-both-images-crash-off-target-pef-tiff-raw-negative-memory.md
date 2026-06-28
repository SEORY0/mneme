---
type: causal-policy
title: "Generic Crash Both Images Crash Off Target Pef Tiff Raw Negative Memory"
description: "Round 13 negative memory for generic_crash with verifier signal both_images_crash_off_target."
failure_class: "generic_crash"
verifier_signal: "both_images_crash_off_target"
candidate_family: "construct"
input_format: "pef-tiff-raw"
harness_convention: "libfuzzer"
vuln_class: "exception-handling-logic"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crash-off-target", "pef-tiff-raw", "negative-memory", "round-13"]
match_keys: ["generic_crash", "both_images_crash_off_target", "pef-tiff-raw", "libfuzzer", "exception-handling-logic", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# Generic Crash Both Images Crash Off Target Pef Tiff Raw Negative Memory

- key: `generic_crash x both_images_crash_off_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pef-tiff-raw]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Minimal TIFF and PEF-like structures did not reproduce the RawSpeed decodeUncompressed exception-handling behavior. One malformed TIFF/PEF size relation crashed both images, so it was an off-target parser or wrapper failure rather than the described fixed/vulnerable split.

## Policy
Treat `generic_crash x both_images_crash_off_target` on `pef-tiff-raw` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crash_off_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
PEF is TIFF-derived: byte order and TIFF magic lead to an IFD of typed tags, including image dimensions, compression, strip offsets, byte counts, and camera make/model metadata that influence RawSpeed decoder selection.

## Harness Contract
The RawSpeed fuzzer passes raw file bytes to RawParser and then to the selected decoder. There is no front selector; the parser chooses a decoder from TIFF/RAW metadata and then runs raw decoding and metadata decoding under exception handling.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

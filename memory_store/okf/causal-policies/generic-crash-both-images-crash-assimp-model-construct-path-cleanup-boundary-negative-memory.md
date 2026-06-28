---
type: negative-memory
title: "Generic Crash Both Images Crash Assimp Model Construct Path Cleanup Boundary Negative Memory"
description: "Round 25 negative memory for generic_crash with verifier signal both_images_crash."
failure_class: "generic_crash"
verifier_signal: "both_images_crash"
candidate_family: "construct"
input_format: "assimp-model"
harness_convention: "libfuzzer"
vuln_class: "path-cleanup-boundary"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crash", "assimp-model", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["generic_crash", "both_images_crash", "assimp-model", "libfuzzer", "path-cleanup-boundary", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Generic Crash Both Images Crash Assimp Model Construct Path Cleanup Boundary Negative Memory

- key: `generic_crash x both_images_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[assimp-model]]
- related harness facts: [[libfuzzer]]

## Failure Shape
OBJ material-library attempts reached secondary-file lookup without triggering the cleanup boundary invariant. A Collada image-path attempt did crash in URI decoding, but confirmation and submission showed the fixed image also crashed, so that was a separate non-differential crash family rather than the FileSystemFilter cleanup target.

## Policy
Treat `generic_crash x both_images_crash` on `assimp-model` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

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
The harness accepts raw model bytes without an extension and relies on signature or content-based importer detection. Collada XML and Wavefront OBJ both reach import code; external resource references are the relevant path because the cleanup filter only runs when importers try to open secondary files.

## Harness Contract
The libFuzzer target passes the entire input directly to Assimp's ReadFileFromMemory with standard post-processing enabled. There is no harness-level carving; importer selection and secondary file opening are controlled entirely by model syntax.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 5 attempts.
- Scope: generator repair and basin avoidance only.

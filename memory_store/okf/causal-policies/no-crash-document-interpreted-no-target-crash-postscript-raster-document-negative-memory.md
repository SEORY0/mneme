---
type: causal-policy
title: "No Crash Document Interpreted No Target Crash Postscript Raster Document Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal document_interpreted_no_target_crash."
failure_class: "no_crash"
verifier_signal: "document_interpreted_no_target_crash"
candidate_family: "construct"
input_format: "postscript-raster-document"
harness_convention: "libfuzzer-ghostscript-gstoraster"
vuln_class: "memcpy-param-overlap"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "document-interpreted-no-target-crash", "postscript-raster-document", "libfuzzer-ghostscript-gstoraster", "negative-memory", "round-18"]
match_keys: ["no-crash", "document-interpreted-no-target-crash", "postscript-raster-document", "libfuzzer-ghostscript-gstoraster", "memcpy-param-overlap", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Document Interpreted No Target Crash Postscript Raster Document Negative Memory

- key: `no_crash x document_interpreted_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-raster-document]]
- related harness facts: [[libfuzzer-ghostscript-gstoraster]]

## Failure Shape
- A valid PostScript pattern/tile document reached the Ghostscript raster device without crashing, but it did not drive the bitmap replication path into an overlapping-copy condition.

## Policy
Treat `no_crash x document_interpreted_no_target_crash` on `postscript-raster-document` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `document_interpreted_no_target_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[postscript-raster-document]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ghostscript-gstoraster]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x document_interpreted_no_target_crash`.
- Candidate family: `construct`.
- Basin summary: A valid PostScript pattern/tile document reached the Ghostscript raster device without crashing, but it did not drive the bitmap replication path into an overlapping-copy condition.

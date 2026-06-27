---
type: causal-policy
title: "Not Verified Not Reached 7z Archive Negative Memory"
description: "Round 18 negative memory for not_verified with verifier signal not_reached."
failure_class: "not_verified"
verifier_signal: "not_reached"
candidate_family: "analysis_only"
input_format: "7z archive"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-memory-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["not-verified", "not-reached", "7z-archive", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["not-verified", "not-reached", "7z-archive", "libfuzzer", "uninitialized-memory-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Not Verified Not Reached 7z Archive Negative Memory

- key: `not_verified x not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[7z-archive]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The vulnerable path requires a structurally valid 7z archive whose packed stream inflates to less data than the declared unpack size, while preserving the folder and stream metadata.
- No local 7z builder or seed was available in the extracted tree, so a safe single-field archive mutation was not produced.

## Policy
Treat `not_verified x not_reached` on `7z archive` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[7z-archive]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `not_verified x not_reached`.
- Candidate family: `analysis_only`.
- Basin summary: The vulnerable path requires a structurally valid 7z archive whose packed stream inflates to less data than the declared unpack size, while preserving the folder and stream metadata.

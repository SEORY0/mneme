---
type: causal-policy
title: "Generic Crash Non Target Crash Or Clean Exit TIFF Negative Memory"
description: "Round 18 negative memory for generic_crash with verifier signal non_target_crash_or_clean_exit."
failure_class: "generic_crash"
verifier_signal: "non_target_crash_or_clean_exit"
candidate_family: "seed_mutate"
input_format: "tiff"
harness_convention: "libfuzzer-graphicsmagick-bigtiff-coder"
vuln_class: "unhandled-exception-path"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "non-target-crash-or-clean-exit", "tiff", "libfuzzer-graphicsmagick-bigtiff-coder", "negative-memory", "round-18"]
match_keys: ["generic-crash", "non-target-crash-or-clean-exit", "tiff", "libfuzzer-graphicsmagick-bigtiff-coder", "unhandled-exception-path", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Generic Crash Non Target Crash Or Clean Exit TIFF Negative Memory

- key: `generic_crash x non_target_crash_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tiff]]
- related harness facts: [[libfuzzer-graphicsmagick-bigtiff-coder]]

## Failure Shape
- Several real TIFF seeds reached the coder; planar seeds produced local segmentation faults in the BIGTIFF wrapper, but the official scorer rejected the candidate, indicating a non-target crash or harness-family mismatch rather than the ReadTIFFImage QuantumTransferMode exception path.

## Policy
Treat `generic_crash x non_target_crash_or_clean_exit` on `tiff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `non_target_crash_or_clean_exit`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[tiff]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-graphicsmagick-bigtiff-coder]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `generic_crash x non_target_crash_or_clean_exit`.
- Candidate family: `seed_mutate`.
- Basin summary: Several real TIFF seeds reached the coder; planar seeds produced local segmentation faults in the BIGTIFF wrapper, but the official scorer rejected the candidate, indicating a non-target crash or harness-family mismatch rather than the ReadTIFFImage QuantumTransferMode exception path.

---
type: causal-policy
title: "Generic Crash Off Target Both Images Assimp Model Negative Memory"
description: "Round 18 negative memory for generic_crash with verifier signal off_target_both_images."
failure_class: "generic_crash"
verifier_signal: "off_target_both_images"
candidate_family: "construct"
input_format: "assimp model"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "off-target-both-images", "assimp-model", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["generic-crash", "off-target-both-images", "assimp-model", "libfuzzer", "out-of-bounds-write", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# Generic Crash Off Target Both Images Assimp Model Negative Memory

- key: `generic_crash x off_target_both_images`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[assimp-model]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A constructed PLY model reached Assimp import and post-processing but crashed earlier in triangulation on both vulnerable and fixed images.
- The intended SortByPTypeProcess path requires avoiding earlier post-process assertions while still producing a mesh whose primitive-type split violates the later copy/allocation relation.

## Policy
Treat `generic_crash x off_target_both_images` on `assimp model` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `off_target_both_images`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[assimp-model]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `generic_crash x off_target_both_images`.
- Candidate family: `construct`.
- Basin summary: A constructed PLY model reached Assimp import and post-processing but crashed earlier in triangulation on both vulnerable and fixed images.

---
type: causal-policy
title: "No Crash Scene Preprocessor Reached Clean Exit Assimp Model Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal scene_preprocessor_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "scene_preprocessor_reached_clean_exit"
candidate_family: "seed_mutate_and_construct"
input_format: "assimp-model"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "scene-preprocessor-reached-clean-exit", "assimp-model", "negative-memory", "round-12"]
match_keys: ["no_crash", "scene_preprocessor_reached_clean_exit", "assimp-model", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Scene Preprocessor Reached Clean Exit Assimp Model Negative Memory

- key: `no_crash x scene_preprocessor_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[assimp-model]]
- related harness facts: [[libfuzzer]]

## Failure Shape
OBJ, PLY, glTF, and sparse-texture-coordinate OBJ variants reached Assimp import and post-processing, including ScenePreprocessor, but the importers normalized or rejected the malformed mesh data before a short texture-coordinate buffer could be walked past its allocation.

## Policy
Treat `no_crash x scene_preprocessor_reached_clean_exit` on `assimp-model` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The harness accepts any Assimp-recognized model format from memory. To reach the target, the model must import into a scene containing a mesh with vertex count, face data, and texture coordinate channels. The vulnerable relation is between declared mesh vertex count and allocated per-vertex attribute arrays.

## Harness Contract
The libFuzzer target passes the input buffer directly to Assimp Importer::ReadFileFromMemory with the realtime quality postprocess preset and no filename extension. Format detection is signature/content based, then normal post-processing invokes ScenePreprocessor.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `scene_preprocessor_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

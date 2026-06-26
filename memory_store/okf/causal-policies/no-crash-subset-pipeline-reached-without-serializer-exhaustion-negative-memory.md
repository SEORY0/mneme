---
type: causal-policy
title: No Crash Subset Pipeline Reached Without Serializer Exhaustion Negative Memory
description: Negative memory for no_crash with verifier signal subset_pipeline_reached_without_serializer_exhaustion.
failure_class: no_crash
verifier_signal: subset_pipeline_reached_without_serializer_exhaustion
candidate_family: seed-sweep
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, subset-pipeline-reached-without-serializer-exhaustion, negative_memory]
match_keys: [no-crash, subset-pipeline-reached-without-serializer-exhaustion, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Subset Pipeline Reached Without Serializer Exhaustion Negative Memory

- key: `no_crash x subset_pipeline_reached_without_serializer_exhaustion`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-sweep
- observed_formats: opentype-font

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- Subset-specific font corpus inputs exercised the HarfBuzz subset harness but did not force ClassDefFormat1 serialization to run out of destination space. A better candidate needs a valid font with class-definition data that survives subsetting while constraining or inflating the serialized class table so the serializer must fail for lack of room.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.

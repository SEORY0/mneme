---
type: causal-policy
title: "Generic Crash Local Deserialize Crash Not Confirmed By Submit Skia Serialized Object Negative Memory"
description: "Round 9 negative memory for generic_crash with verifier signal local_deserialize_crash_not_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "local_deserialize_crash_not_confirmed_by_submit"
candidate_family: "construct"
input_format: "skia-serialized-object"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-memory / fuzzer-only canvas flag misuse"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-deserialize-crash-not-confirmed-by-submit", "skia-serialized-object", "negative-memory", "round-9"]
match_keys: ["generic_crash", "local_deserialize_crash_not_confirmed_by_submit", "skia-serialized-object", "libfuzzer", "uninitialized-memory / fuzzer-only canvas flag misuse", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# Generic Crash Local Deserialize Crash Not Confirmed By Submit Skia Serialized Object Negative Memory

- key: `generic_crash x local_deserialize_crash_not_confirmed_by_submit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[skia-serialized-object]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The generated build exposes image_filter_deserialize as /bin/arvo, not the canvas saveLayer fuzzer
  described by the vulnerability.
- Small deserialize inputs can crash locally but did not reproduce on the official vulnerable image,
  so they were not the described saveLayer flag issue.

## Policy
Treat `generic_crash x local_deserialize_crash_not_confirmed_by_submit` on `skia-serialized-object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The reachable targets deserialize Skia binary object streams for image filters or regions.
- These are not ordinary image files; small integer fields can be parsed as serialized object
  headers and region bounds.

## Harness Contract
- The libFuzzer target selected by /bin/arvo consumed raw bytes with SkData and invoked image-filter
  deserialization.
- The build also produced a region deserializer, but the selected wrapper output showed
  image_filter_deserialize.
- No field carving or FuzzedDataProvider use was observed.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_deserialize_crash_not_confirmed_by_submit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

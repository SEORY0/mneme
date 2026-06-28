---
type: causal-policy
title: "Generic Crash Sink Mismatch Skia Serialized Image Filter Negative Memory"
description: "Round 9 negative memory for generic_crash with verifier signal sink_mismatch."
failure_class: "generic_crash"
verifier_signal: "sink_mismatch"
candidate_family: "construct|negative_control"
input_format: "skia-serialized-image-filter"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "sink-mismatch", "skia-serialized-image-filter", "negative-memory", "round-9"]
match_keys: ["generic_crash", "sink_mismatch", "skia-serialized-image-filter", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# Generic Crash Sink Mismatch Skia Serialized Image Filter Negative Memory

- key: `generic_crash x sink_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[skia-serialized-image-filter]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Empty and random serialized-filter inputs produced low-likelihood generic crashes, while image-
  file bytes and invalid image resources were cleanly rejected.
- None reached the described SkPictureShader::onMakeContext path; the missing ingredient is a valid
  serialized SkImageFilter graph containing a picture shader whose rasterization returns EmptyShader
  without initializing the scale-adjust vector.

## Policy
Treat `generic_crash x sink_mismatch` on `skia-serialized-image-filter` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The target format is Skia's internal flattened SkImageFilter serialization, not a PNG/JPEG/GIF
  image.
- A useful input must deserialize into an image filter object graph; to reach the described bug it
  likely needs a paint/shader branch containing a serialized picture shader and dimensions or tile
  state that force the EmptyShader path.

## Harness Contract
- The harness passes raw bytes directly to SkImageFilter::Deserialize and then exercises the
  deserialized filter at a fixed width.
- There is no mode selector or external image file contract.
- Ordinary encoded image bytes are treated as serialized-filter bytes and usually fail
  deserialization.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `sink_mismatch`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

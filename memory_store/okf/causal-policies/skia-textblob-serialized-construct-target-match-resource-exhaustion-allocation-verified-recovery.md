---
type: causal-policy
title: "Skia Textblob Serialized Construct Target Match Resource Exhaustion Allocation Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal target_match."
failure_class: "generic_crash"
verifier_signal: "target_match"
candidate_family: "construct"
input_format: "skia-textblob-serialized"
harness_convention: "libfuzzer"
vuln_class: "resource-exhaustion-allocation"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match", "skia-textblob-serialized", "libfuzzer", "construct", "resource-exhaustion-allocation", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "target_match", "skia-textblob-serialized", "libfuzzer", "resource-exhaustion-allocation", "verified_recovery", "construct", "other"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Skia Textblob Serialized Construct Target Match Resource Exhaustion Allocation Verified Recovery

## Policy
For `generic_crash x target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a readable SkTextBlob serialization from scratch, not an image seed. Satisfy the raw SkReadBuffer alignment and the text-blob envelope enough to pass bounds, run positioning, paint, and text-encoding checks. Then declare an extremely large positive glyph count in a run but omit the corresponding glyph and position payloads. The vulnerable deserializer allocates run storage from the declared count before checking that the serialized payload is present; the fixed build rejects the short payload before allocation.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[skia-textblob-serialized]]: A serialized SkTextBlob begins with rectangle bounds, followed by repeated runs and a zero-glyph-count end marker. Each run stores a glyph count, a packed positioning/extended flag word, optional text byte count, a point offset, a flattened paint, then length-prefixed glyph and position byte arrays, plus cluster and text arrays for extended runs. The paint must deserialize with glyph-id text encoding for the builder to allocate a run. The top-level size must be word-aligned for SkReadBuffer to accept the input.
- Harness [[libfuzzer]]: The libFuzzer entrypoint passes the raw input bytes directly into a SkReadBuffer and calls SkTextBlob::MakeFromBuffer. There is no mode selector and no FuzzedDataProvider. After deserialization the harness checks only the buffer validity, creates a small raster surface, and draws the blob at a fixed positive translation; ordinary positive bounds can be quick-rejected before glyph replay, so reachable drawing-oriented tests need bounds that intersect after that translation. The allocation bug triggers during deserialization, before the draw step.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[skia-textblob-serialized]] and [[libfuzzer]].

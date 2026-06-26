---
type: causal-policy
title: "MVG Construct Geometry Radius Verified Recovery"
description: "Round 6 verified recovery for generic_crash with verifier signal sanitizer_or_process_crash_after_mvg_parser."
failure_class: "generic_crash"
verifier_signal: "sanitizer_or_process_crash_after_mvg_parser"
candidate_family: "construct_geometry_radius"
input_format: "mvg"
harness_convention: "libfuzzer raw MVG blob"
vuln_class: "arithmetic-overflow-to-renderer-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "sanitizer-or-process-crash-after-mvg-parser", "mvg", "construct-geometry-radius", "verified-recovery", "round-6"]
match_keys: ["generic_crash", "sanitizer_or_process_crash_after_mvg_parser", "mvg", "libfuzzer raw MVG blob", "arithmetic-overflow-to-renderer-crash", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# MVG Construct Geometry Radius Verified Recovery

## Policy
For `generic_crash x sanitizer_or_process_crash_after_mvg_parser`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a minimal MVG drawing with a viewbox first and a single ellipse primitive. Keep the canvas small, use ordinary angles and non-negative radii, then grow only the radius as a plain decimal until the renderer crosses the arithmetic boundary in primitive tracing; avoid extra primitives or trailing noise.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- MVG is line-oriented text. The reader recognizes the format from a leading viewbox-style line, uses that viewbox to allocate the canvas, then renders subsequent primitive commands such as ellipse, polygon, path, and line. Geometry fields parse as decimal numbers; radius values must remain syntactically valid and non-negative.
- Harness: The GraphicsMagick coder fuzzer feeds the entire file as raw bytes to the MVG coder. There is no leading selector byte or FuzzedDataProvider splitting; the first accepted MVG header line is the main parser gate.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

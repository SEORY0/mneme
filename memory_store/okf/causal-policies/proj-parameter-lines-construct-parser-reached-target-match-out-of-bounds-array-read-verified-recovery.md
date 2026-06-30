---
type: causal-policy
title: "Proj Parameter Lines Construct Parser Reached Target Match Out Of Bounds Array Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "proj-parameter-lines"
harness_convention: "afl-libfuzzer-compatible"
vuln_class: "out-of-bounds-array-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "proj-parameter-lines", "afl-libfuzzer-compatible", "construct", "out-of-bounds-array-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_target_match", "proj-parameter-lines", "afl-libfuzzer-compatible", "out-of-bounds-array-read", "verified_recovery", "construct", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Proj Parameter Lines Construct Parser Reached Target Match Out Of Bounds Array Read Verified Recovery

## Policy
For `generic_crash x parser_reached_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Satisfy the three-line PROJ fuzzer contract with a source definition, destination definition, and finite three-dimensional coordinate tuple. Make the source definition a one-step transformation pipeline whose unit-conversion step declares only one side of a time-unit conversion while otherwise keeping spatial unit names valid. Force the transform to run the source pipeline in reverse through the three-dimensional path; the reverse time conversion indexes the time-unit table with the missing opposite-side unit identifier.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[proj-parameter-lines]]: The fuzzer input is newline-delimited PROJ text followed by a coordinate record. Projection definitions are plus-parameter strings parsed by the PROJ initializer. The coordinate record may be textual or a binary two-dimensional or three-dimensional tuple; the three-dimensional binary form is needed when the transform path must call projection three-dimensional callbacks. Pipeline definitions use step markers, and unit-conversion parameters are exact symbolic unit names looked up during initialization.
- Harness [[afl-libfuzzer-compatible]]: The harness copies raw input bytes, appends a terminator, splits on the first two newlines, initializes both PROJ definitions, and calls the transform routine on one coordinate. Inputs that fail either initializer exit cleanly before the vulnerable path. No FuzzedDataProvider carving is used.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[proj-parameter-lines]] and [[afl-libfuzzer-compatible]].

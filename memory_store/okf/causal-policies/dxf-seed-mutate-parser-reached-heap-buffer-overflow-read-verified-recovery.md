---
type: causal-policy
title: "Dxf Seed Mutate Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "dxf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "dxf", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached", "dxf", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "seed-mutate", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Dxf Seed Mutate Parser Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Mutate a real DXF seed containing a TABLEGEOMETRY object. Keep the object header and first cell-start group valid, make the initial cell count allocate a zero-sized cell array, then let a later duplicate count make destruction or output traversal believe cells exist before the helper can repair the pointer with a real allocation.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[dxf]]: DXF is parsed as code/value line pairs. TABLEGEOMETRY uses scalar groups for row count, column count, and cell count, followed by repeated cell groups with a cell-start marker, dimensions, handles, geometry count, and optional geometry subrecords. Duplicate scalar groups can update object fields later in the same object.
- Harness [[libfuzzer]]: The libFuzzer target consumes the raw input as a file buffer. Inputs beginning like AutoCAD text are routed through the DXF reader, then the harness may exercise output conversion before final object cleanup; there is no mode byte or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[dxf]] and [[libfuzzer]].

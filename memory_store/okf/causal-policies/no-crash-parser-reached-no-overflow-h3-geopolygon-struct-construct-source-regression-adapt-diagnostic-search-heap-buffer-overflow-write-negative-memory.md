---
type: negative-memory
title: "No Crash Parser Reached No Overflow H3 Geopolygon Struct Construct Source Regression Adapt Diagnostic Search Heap Buffer Overflow Write Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal parser_reached_no_overflow."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_overflow"
candidate_family: "construct|source_regression_adapt|diagnostic_search"
input_format: "h3-geopolygon-struct"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-overflow", "h3-geopolygon-struct", "libfuzzer", "construct-source-regression-adapt-diagnostic-search", "negative-memory", "round-26"]
match_keys: ["no_crash", "parser_reached_no_overflow", "h3-geopolygon-struct", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Parser Reached No Overflow H3 Geopolygon Struct Construct Source Regression Adapt Diagnostic Search Heap Buffer Overflow Write Negative Memory

- key: `no_crash x parser_reached_no_overflow`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h3-geopolygon-struct]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The correct full-struct harness layout was reached, but the tested polygons did not make the experimental size estimator undercount relative to the writer. Adapted no-holes regression data, world-scale polygons, transmeridian and pole-adjacent rectangles, degenerate lines/points, reported issue rectangles, simple holes, and targeted cell-boundary-derived shapes all executed without an overflow signal.

## Policy
Treat `no_crash x parser_reached_no_overflow` on `h3-geopolygon-struct` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_no_overflow` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_overflow`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The H3 input describes a polygon: a resolution field, a hole-count field, then loop records. Each loop record contains a vertex count followed by latitude/longitude coordinate pairs, and hole loops repeat that same record shape. The experimental max-size routine estimates using overlapping bounding boxes and compact cells, while the writer iterates cells using the requested containment mode.

## Harness Contract
The libFuzzer harness requires a fixed-size native struct-shaped input rather than a plain vertex blob. Integral fields are read directly from the front of the buffer using native little-endian layout. The remaining buffer is parsed front-to-back as the outer loop and then optional hole loops. For each input, the harness runs every valid containment mode once with the original hole count and once with holes disabled.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 12 attempts.
- Scope: generator repair and basin avoidance only.

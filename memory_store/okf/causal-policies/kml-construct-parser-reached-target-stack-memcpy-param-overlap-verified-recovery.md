---
type: causal-policy
title: "KML Construct Parser Reached Target Stack Memcpy Param Overlap Verified Recovery"
description: "Round 8 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "kml"
harness_convention: "libfuzzer"
vuln_class: "memcpy-param-overlap"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "kml", "construct", "verified-recovery", "round-8"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "kml", "libfuzzer", "memcpy-param-overlap", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# KML Construct Parser Reached Target Stack Memcpy Param Overlap Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a raw KML document whose root is visible in the file header. Keep the document in the all-empty-container mode by using feature containers without geometry, but include a folder that first accumulates many empty folder children and then contains a feature container. This makes layer discovery preserve empty folders as layers, then eliminate an early empty child from a layer array with later entries, triggering overlapping pointer-array compaction.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The KML driver recognizes raw XML content by a visible KML root element in the header, then parses nested Document and Folder containers plus Placemark feature containers. Geometry-bearing placemarks make the normal pre-layer empty-elimination path run; placemarks without geometry can keep the tree in the all-empty mode where empty folders are still considered during layer discovery.
- Harness: The libFuzzer harness writes the exact input bytes to an in-memory file named without a KML extension, registers OGR drivers, opens that memory file read-only through OGR, iterates all layers and features if open succeeds, and destroys the datasource. There is no selector byte or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

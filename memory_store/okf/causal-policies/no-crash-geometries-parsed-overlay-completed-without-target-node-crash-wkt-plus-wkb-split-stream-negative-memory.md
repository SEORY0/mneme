---
type: causal-policy
title: "No Crash Geometries Parsed Overlay Completed Without Target Node Crash Wkt Plus Wkb Split Stream Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal geometries_parsed_overlay_completed_without_target_node_crash."
failure_class: "no_crash"
verifier_signal: "geometries_parsed_overlay_completed_without_target_node_crash"
candidate_family: "construct_and_seed_from_geos_cases"
input_format: "wkt-plus-wkb-split-stream"
harness_convention: "libfuzzer raw bytes with nul split"
vuln_class: "geometry-overlay-edge-node-lifetime-or-coordinate-mismatch"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "geometries-parsed-overlay-completed-without-target-node-crash", "wkt-plus-wkb-split-stream", "libfuzzer-raw-bytes-with-nul-split", "construct-and-seed-from-geos-cases", "negative-memory", "round-24"]
match_keys: ["no-crash", "geometries-parsed-overlay-completed-without-target-node-crash", "wkt-plus-wkb-split-stream", "libfuzzer-raw-bytes-with-nul-split", "geometry-overlay-edge-node-lifetime-or-coordinate-mismatch"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Geometries Parsed Overlay Completed Without Target Node Crash Wkt Plus Wkb Split Stream Negative Memory

- key: `no_crash x geometries_parsed_overlay_completed_without_target_node_crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[wkt-plus-wkb-split-stream]]
- harnesses: [[libfuzzer-raw-bytes-with-nul-split]]

## Dead-End Shape
Valid WKT and WKB geometry pairs reached the GEOS overlay operations, including cases derived from robustness tests, but did not create the specific EdgeEnd/Node insertion invariant violation needed for the described crash.

## Policy
For `no_crash x geometries_parsed_overlay_completed_without_target_node_crash` on `wkt-plus-wkb-split-stream`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct_and_seed_from_geos_cases` only while this format and harness contract are present.

## Procedure
1. When `no_crash x geometries_parsed_overlay_completed_without_target_node_crash` appears for `wkt-plus-wkb-split-stream`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.

---
type: negative-memory
title: "No Crash Wrapper Usage Or Parser Not Reached Dxf Text Construct Heap Buffer Overflow Write Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal wrapper_usage_or_parser_not_reached."
failure_class: "no_crash"
verifier_signal: "wrapper_usage_or_parser_not_reached"
candidate_family: "construct"
input_format: "dxf-text"
harness_convention: "honggfuzz/libfuzzer wrapper"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-usage-or-parser-not-reached", "dxf-text", "honggfuzz-libfuzzer-wrapper", "construct", "negative-memory", "round-23"]
match_keys: ["no-crash", "wrapper-usage-or-parser-not-reached", "dxf-text", "honggfuzz-libfuzzer-wrapper", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Wrapper Usage Or Parser Not Reached Dxf Text Construct Heap Buffer Overflow Write Negative Memory

- key: `no_crash x wrapper_usage_or_parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dxf-text]]
- harnesses: [[honggfuzz-libfuzzer-wrapper]]

## Failure Shape
Minimal OBJECTS-section SPATIAL_FILTER records with matrix entries, count fields, and clip-vertex fields did not produce an observable crash under the local wrapper. The likely missing gate is a fuller LibreDWG object scaffold or version/class state that makes the SPATIAL_FILTER object accepted before the dynapi field loop.

## Policy
Treat `no_crash x wrapper_usage_or_parser_not_reached` on `dxf-text` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser, envelope, or harness contract that the trace showed was reached.
2. Identify the missing causal relation from the verifier signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, nonreproducible, or both-crash basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 23 after 4 attempts.
- Scope: generator repair and basin avoidance only.

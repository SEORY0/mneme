---
type: negative-memory
title: "No Crash MXF Demuxer Completed Quickly MXF Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal mxf_demuxer_completed_quickly."
failure_class: "no_crash"
verifier_signal: "mxf_demuxer_completed_quickly"
candidate_family: "construct"
input_format: "mxf"
harness_convention: "libfuzzer"
vuln_class: "algorithmic-complexity"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mxf-demuxer-completed-quickly", "mxf", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "mxf-demuxer-completed-quickly", "mxf", "libfuzzer", "algorithmic-complexity"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash MXF Demuxer Completed Quickly MXF Negative Memory

- key: `no_crash x mxf_demuxer_completed_quickly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mxf]]
- harnesses: [[libfuzzer]]

## Failure Shape
A minimal MXF-like header was accepted only as a quick non-crashing demuxer input and did not create the dense index-table state needed for the performance issue. A likely solution needs many valid index table segments and edit-unit lookup requests arranged so absolute-offset lookup performs repeated linear scans.

## Policy
Treat `no_crash x mxf_demuxer_completed_quickly` on `mxf` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.

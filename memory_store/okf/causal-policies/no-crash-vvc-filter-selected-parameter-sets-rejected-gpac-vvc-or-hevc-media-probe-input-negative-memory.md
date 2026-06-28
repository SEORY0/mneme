---
type: negative-memory
title: "No Crash Vvc Filter Selected Parameter Sets Rejected Gpac Vvc Or Hevc Media Probe Input Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal vvc_filter_selected_parameter_sets_rejected."
failure_class: "no_crash"
verifier_signal: "vvc_filter_selected_parameter_sets_rejected"
candidate_family: "construct_vvc_annexb_and_seed_mp4_probe"
input_format: "gpac-vvc-or-hevc-media-probe-input"
harness_convention: "libfuzzer-gpac-probe-analyze"
vuln_class: "vvc-tile-parser-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "vvc-filter-selected-parameter-sets-rejected", "gpac-vvc-or-hevc-media-probe-input", "libfuzzer-gpac-probe-analyze", "construct-vvc-annexb-and-seed-mp4-probe", "negative-memory", "round-19"]
match_keys: ["no-crash", "vvc-filter-selected-parameter-sets-rejected", "gpac-vvc-or-hevc-media-probe-input", "libfuzzer-gpac-probe-analyze", "vvc-tile-parser-bounds"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Vvc Filter Selected Parameter Sets Rejected Gpac Vvc Or Hevc Media Probe Input Negative Memory

- key: `no_crash x vvc_filter_selected_parameter_sets_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gpac-vvc-or-hevc-media-probe-input]]
- harnesses: [[libfuzzer-gpac-probe-analyze]]

## Failure Shape
Synthetic VVC and HEVC Annex-B-like streams were recognized by GPAC probe/analyze as video elementary streams, and MP4 samples were probed as valid non-target media, but the parameter sets and slice headers were rejected before tile state was configured. The missing relation is coherent VVC parameter-set and picture-header data that reaches tile parsing before introducing the corrupted tile-count or tile-boundary invariant.

## Policy
Treat `no_crash x vvc_filter_selected_parameter_sets_rejected` on `gpac-vvc-or-hevc-media-probe-input` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

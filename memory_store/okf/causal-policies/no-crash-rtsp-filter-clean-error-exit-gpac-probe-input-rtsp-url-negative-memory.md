---
type: negative-memory
title: "No Crash Rtsp Filter Clean Error Exit Gpac Probe Input Rtsp Url Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal rtsp_filter_clean_error_exit."
failure_class: "no_crash"
verifier_signal: "rtsp_filter_clean_error_exit"
candidate_family: "construct"
input_format: "gpac-probe-input-rtsp-url"
harness_convention: "libfuzzer"
vuln_class: "stack-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "rtsp-filter-clean-error-exit", "gpac-probe-input-rtsp-url", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "rtsp-filter-clean-error-exit", "gpac-probe-input-rtsp-url", "libfuzzer", "stack-overflow"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Rtsp Filter Clean Error Exit Gpac Probe Input Rtsp Url Negative Memory

- key: `no_crash x rtsp_filter_clean_error_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gpac-probe-input-rtsp-url]]
- harnesses: [[libfuzzer]]

## Failure Shape
Raw RTSP URLs with long hosts, repeated credentials, deep slash paths, malformed bracketed hosts, and percent-heavy queries reached GPAC filter setup but exited through unsupported or network-unreachable errors. SDP wrappers were not recognized by the probe/analyze graph in these forms.

## Policy
Treat `no_crash x rtsp_filter_clean_error_exit` on `gpac-probe-input-rtsp-url` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

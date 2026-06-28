---
type: negative-memory
title: "No Crash Clean Media Inspect Or Probe Reject Gpac Media Or Av1 Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal clean-media-inspect-or-probe-reject."
failure_class: "no-crash"
verifier_signal: "clean-media-inspect-or-probe-reject"
candidate_family: "seed-sweep-and-construct"
input_format: "gpac-media-or-av1"
harness_convention: "libfuzzer-raw-gpac-probe-analyze"
vuln_class: "memory-overread"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-media-inspect-or-probe-reject", "gpac-media-or-av1", "libfuzzer-raw-gpac-probe-analyze", "seed-sweep-and-construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "clean-media-inspect-or-probe-reject", "gpac-media-or-av1", "libfuzzer-raw-gpac-probe-analyze", "memory-overread"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Clean Media Inspect Or Probe Reject Gpac Media Or Av1 Negative Memory

- key: `no-crash x clean-media-inspect-or-probe-reject`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gpac-media-or-av1]]
- harnesses: [[libfuzzer-raw-gpac-probe-analyze]]

## Failure Shape
Shipped MP4 samples exercised GPAC inspection successfully but used non-target codecs, while small IVF and raw OBU-like probes were rejected or skipped before a configured AV1 output stream existed. The missing invariant is a broken AV1 stream that is still sufficiently configured for the AV1 analyzer/dumper before exposing the overread.

## Policy
Treat `no-crash x clean-media-inspect-or-probe-reject` on `gpac-media-or-av1` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.

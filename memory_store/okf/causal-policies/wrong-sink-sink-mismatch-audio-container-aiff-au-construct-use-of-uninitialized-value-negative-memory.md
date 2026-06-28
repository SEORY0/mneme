---
type: negative-memory
title: "Wrong Sink Sink Mismatch Audio Container Aiff Au Construct Use Of Uninitialized Value Negative Memory"
description: "Round 23 negative memory for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "audio-container-aiff-au"
harness_convention: "libfuzzer-libsndfile-virtual-io"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "sink-mismatch", "audio-container-aiff-au", "libfuzzer-libsndfile-virtual-io", "construct", "negative-memory", "round-23"]
match_keys: ["wrong-sink", "sink-mismatch", "audio-container-aiff-au", "libfuzzer-libsndfile-virtual-io", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# Wrong Sink Sink Mismatch Audio Container Aiff Au Construct Use Of Uninitialized Value Negative Memory

- key: `wrong_sink x sink_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[audio-container-aiff-au]]
- harnesses: [[libfuzzer-libsndfile-virtual-io]]

## Failure Shape
AIFF-C float/double containers with intentionally short sample data reached libsndfile parsing and produced MemorySanitizer crashes, but the observed sink was a logging/path validation use rather than the target endian-swap array path; the official fixed image also failed, so it was not a solve. AU double variants did not reach the uninitialized swap path.

## Policy
Treat `wrong_sink x sink_mismatch` on `audio-container-aiff-au` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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

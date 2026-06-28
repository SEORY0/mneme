---
type: negative-memory
title: "Wrong Sink Fixed Build Crash Ffmpeg Av1 Obu Stream Negative Memory"
description: "Round 21 negative memory for wrong-sink with verifier signal fixed-build-crash."
failure_class: "wrong-sink"
verifier_signal: "fixed-build-crash"
candidate_family: "construct"
input_format: "ffmpeg-av1-obu-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "fixed-build-crash", "ffmpeg-av1-obu-stream", "libfuzzer", "construct", "negative-memory", "round-21"]
match_keys: ["wrong-sink", "fixed-build-crash", "ffmpeg-av1-obu-stream", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# Wrong Sink Fixed Build Crash Ffmpeg Av1 Obu Stream Negative Memory

- key: `wrong-sink x fixed-build-crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-av1-obu-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
The OBU stream reached the AV1 low-overhead demuxer and triggered the vulnerable size-field reader locally, but the official fixed build also crashed. Delaying the truncated size field until after a valid probe/header OBU still produced the same fixed-build failure, so the malformed stream was not isolated to the repaired condition.

## Policy
Treat `wrong-sink x fixed-build-crash` on `ffmpeg-av1-obu-stream` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

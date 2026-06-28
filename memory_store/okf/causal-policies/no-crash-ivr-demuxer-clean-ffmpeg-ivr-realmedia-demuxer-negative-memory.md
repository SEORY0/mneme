---
type: negative-memory
title: "No Crash Ivr Demuxer Clean Ffmpeg Ivr Realmedia Demuxer Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal ivr-demuxer-clean."
failure_class: "no-crash"
verifier_signal: "ivr-demuxer-clean"
candidate_family: "seed-mutate-and-construct"
input_format: "ffmpeg-ivr-realmedia-demuxer"
harness_convention: "libfuzzer-ffmpeg-demuxer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ivr-demuxer-clean", "ffmpeg-ivr-realmedia-demuxer", "libfuzzer-ffmpeg-demuxer", "seed-mutate-and-construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "ivr-demuxer-clean", "ffmpeg-ivr-realmedia-demuxer", "libfuzzer-ffmpeg-demuxer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Ivr Demuxer Clean Ffmpeg Ivr Realmedia Demuxer Negative Memory

- key: `no-crash x ivr-demuxer-clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-ivr-realmedia-demuxer]]
- harnesses: [[libfuzzer-ffmpeg-demuxer]]

## Failure Shape
RealMedia/RealAudio seed truncations and direct IVR constructions with RealAudio OpaqueData and short advertised packet bodies all exited cleanly. The active binary is the IVR demuxer; the missing trigger likely requires a more exact RealAudio interleaver state where a partial read is later consumed before clean error handling.

## Policy
Treat `no-crash x ivr-demuxer-clean` on `ffmpeg-ivr-realmedia-demuxer` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

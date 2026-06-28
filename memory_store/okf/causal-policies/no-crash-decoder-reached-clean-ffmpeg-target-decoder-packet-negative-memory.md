---
type: negative-memory
title: "No Crash Decoder Reached Clean Ffmpeg Target Decoder Packet Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal decoder_reached_clean."
failure_class: "no_crash"
verifier_signal: "decoder_reached_clean"
candidate_family: "construct"
input_format: "ffmpeg-target-decoder-packet"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-reached-clean", "ffmpeg-target-decoder-packet", "libfuzzer", "construct", "negative-memory", "round-22"]
match_keys: ["no-crash", "decoder-reached-clean", "ffmpeg-target-decoder-packet", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Decoder Reached Clean Ffmpeg Target Decoder Packet Negative Memory

- key: `no_crash x decoder_reached_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-target-decoder-packet]]
- harnesses: [[libfuzzer]]

## Failure Shape
The task metadata said tar, but the active wrapper ran the H263I target decoder fuzzer on raw bytes. Direct H264-like, HEVC-like, MPEG-like, random start-code, and tar-wrapped carriers all reached clean decoder execution and reported decoded pixels, but did not create the missing-slice condition that exposes uninitialized frame-buffer content.

## Policy
Treat `no_crash x decoder_reached_clean` on `ffmpeg-target-decoder-packet` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, wrapper-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 22.
- Scope: generator repair and basin avoidance only.

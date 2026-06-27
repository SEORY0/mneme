---
type: negative-memory
title: "No Crash Sws 16bit Scaler Clean Official Ffmpeg Sws Fuzzer Frame Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal sws_16bit_scaler_clean_official."
failure_class: "no_crash"
verifier_signal: "sws_16bit_scaler_clean_official"
candidate_family: "construct"
input_format: "ffmpeg-sws-fuzzer-frame"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-memory"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "sws-16bit-scaler-clean-official", "ffmpeg-sws-fuzzer-frame", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "sws-16bit-scaler-clean-official", "ffmpeg-sws-fuzzer-frame", "libfuzzer", "use-of-uninitialized-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Sws 16bit Scaler Clean Official Ffmpeg Sws Fuzzer Frame Negative Memory

- key: `no_crash x sws_16bit_scaler_clean_official`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-sws-fuzzer-frame]]
- harnesses: [[libfuzzer]]

## Failure Shape
The first media-file seed was the wrong envelope. A constructed SWS envelope reached ffmpeg_SWS_fuzzer and converted a 16-bit grayscale source to an 8-bit destination, but both local and official runs stayed clean. The missing condition is likely a sliced or threaded scaling configuration that leaves allocated slice lines uninitialized before hScale16To15_c consumes them.

## Policy
Treat `no_crash x sws_16bit_scaler_clean_official` on `ffmpeg-sws-fuzzer-frame` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

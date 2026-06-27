---
type: negative-memory
title: "No Crash Mpegvideo Decoder Reached Clean Ffmpeg Mpegvideo Target Decoder Packets Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal mpegvideo_decoder_reached_clean."
failure_class: "no_crash"
verifier_signal: "mpegvideo_decoder_reached_clean"
candidate_family: "seed_mutate_h264_then_mpegvideo_elementary_streams"
input_format: "ffmpeg-mpegvideo-target-decoder-packets"
harness_convention: "oss-fuzz-run-poc-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mpegvideo-decoder-reached-clean", "ffmpeg-mpegvideo-target-decoder-packets", "oss-fuzz-run-poc-ffmpeg-target-decoder", "seed-mutate-h264-then-mpegvideo-elementary-streams", "negative-memory", "round-19"]
match_keys: ["no-crash", "mpegvideo-decoder-reached-clean", "ffmpeg-mpegvideo-target-decoder-packets", "oss-fuzz-run-poc-ffmpeg-target-decoder", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Mpegvideo Decoder Reached Clean Ffmpeg Mpegvideo Target Decoder Packets Negative Memory

- key: `no_crash x mpegvideo_decoder_reached_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-mpegvideo-target-decoder-packets]]
- harnesses: [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

## Failure Shape
Verifier output showed the active decoder was MPEGVIDEO, not the initially assumed H.264 target. H.264 seeds still decoded under the selected decoder, and MPEG video program/elementary-stream seeds plus truncation, gap, and short-slice mutations reached decoding with pixel output but did not expose an uninitialized missing-slice state.

## Policy
Treat `no_crash x mpegvideo_decoder_reached_clean` on `ffmpeg-mpegvideo-target-decoder-packets` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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

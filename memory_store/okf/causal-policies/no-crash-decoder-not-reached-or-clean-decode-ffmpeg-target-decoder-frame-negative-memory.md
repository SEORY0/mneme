---
type: causal-policy
title: "No Crash Decoder Not Reached Or Clean Decode Ffmpeg Target Decoder Frame Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal decoder_not_reached_or_clean_decode."
failure_class: "no_crash"
verifier_signal: "decoder_not_reached_or_clean_decode"
candidate_family: "seed_mutate"
input_format: "ffmpeg-target-decoder-frame"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-not-reached-or-clean-decode", "ffmpeg-target-decoder-frame", "negative-memory", "round-13"]
match_keys: ["no_crash", "decoder_not_reached_or_clean_decode", "ffmpeg-target-decoder-frame", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Decoder Not Reached Or Clean Decode Ffmpeg Target Decoder Frame Negative Memory

- key: `no_crash x decoder_not_reached_or_clean_decode`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-target-decoder-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Real WMAVoice ASF samples and synthetic decoder-fuzzer envelopes did not reach the pitch-dependent uninitialized-value path. The likely missing ingredient is extracting valid raw WMAVoice decoder packets and exact codec extradata from the container rather than feeding ASF bytes or guessed context tails.

## Policy
Treat `no_crash x decoder_not_reached_or_clean_decode` on `ffmpeg-target-decoder-frame` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_not_reached_or_clean_decode`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The FFmpeg target decoder fuzzer treats the front of the input as one or more raw packet regions separated by a fixed split tag. When the input is large enough, a fixed-size tail configures codec context fields and optional extradata before avcodec_open2 and packet decoding.

## Harness Contract
The target is the WMAVoice decoder fuzzer, not the ASF demuxer. It consumes raw decoder packets plus the decoder-fuzzer configuration tail; container bytes alone do not necessarily provide codec extradata or valid packet boundaries.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

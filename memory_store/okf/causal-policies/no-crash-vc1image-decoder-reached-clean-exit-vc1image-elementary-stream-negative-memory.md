---
type: causal-policy
title: "No Crash Vc1image Decoder Reached Clean Exit Vc1image Elementary Stream Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal vc1image_decoder_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "vc1image_decoder_reached_clean_exit"
candidate_family: "seed_mutate"
input_format: "vc1image-elementary-stream"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "vc1image-decoder-reached-clean-exit", "vc1image-elementary-stream", "negative-memory", "round-13"]
match_keys: ["no_crash", "vc1image_decoder_reached_clean_exit", "vc1image-elementary-stream", "libfuzzer-ffmpeg-target-decoder", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Vc1image Decoder Reached Clean Exit Vc1image Elementary Stream Negative Memory

- key: `no_crash x vc1image_decoder_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[vc1image-elementary-stream]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
Real VC1 and RCV samples reached the VC1IMAGE decoder fuzzer and executed cleanly. The missing condition is likely an image-coded VC1 frame shape that reaches macroblock decoding with skipped or reused block metadata, rather than ordinary video elementary streams.

## Policy
Treat `no_crash x vc1image_decoder_reached_clean_exit` on `vc1image-elementary-stream` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `vc1image_decoder_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The target consumes raw VC1-family decoder payloads rather than a media container. The active binary is the VC1IMAGE decoder fuzzer; ordinary VC1/RCV elementary streams can be accepted but may not drive the exact image-coded macroblock path tied to the uninitialized mb_type and transform-type tables.

## Harness Contract
The FFmpeg target decoder fuzzer runs a fixed decoder on the raw input file, optionally through FFmpeg parser logic, with no outer container required and no FuzzedDataProvider fields in front of the codec bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

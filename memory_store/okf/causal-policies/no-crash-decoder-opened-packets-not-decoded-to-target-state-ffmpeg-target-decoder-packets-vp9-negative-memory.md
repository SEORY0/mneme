---
type: causal-policy
title: "No Crash Decoder Opened Packets Not Decoded To Target State Ffmpeg Target Decoder Packets VP9 Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal decoder_opened_packets_not_decoded_to_target_state."
failure_class: "no_crash"
verifier_signal: "decoder_opened_packets_not_decoded_to_target_state"
candidate_family: "construct-and-seed-mutate"
input_format: "ffmpeg-target-decoder-packets-vp9"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "decoder-opened-packets-not-decoded-to-target-state", "ffmpeg-target-decoder-packets-vp9", "libfuzzer-ffmpeg-target-decoder", "negative-memory", "round-18"]
match_keys: ["no-crash", "decoder-opened-packets-not-decoded-to-target-state", "ffmpeg-target-decoder-packets-vp9", "libfuzzer-ffmpeg-target-decoder", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Decoder Opened Packets Not Decoded To Target State Ffmpeg Target Decoder Packets VP9 Negative Memory

- key: `no_crash x decoder_opened_packets_not_decoded_to_target_state`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-target-decoder-packets-vp9]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
- The active verifier target was VP9 rather than the H.264 value visible in the build script.
- H.264-shaped data, synthetic VP9 frame data, a VP9 WebM seed treated as raw packet data, split packet/tag/tail layouts, container fragments, and two synthetic packet layouts all decoded zero frames or only exercised generic packet rejection.
- The missing gate is extracting or constructing raw VP9 frame packets that the target decoder accepts, then creating missing-tile or missing-slice conditions that leave custom-allocated frame buffers partially uninitialized.

## Policy
Treat `no_crash x decoder_opened_packets_not_decoded_to_target_state` on `ffmpeg-target-decoder-packets-vp9` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_opened_packets_not_decoded_to_target_state`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[ffmpeg-target-decoder-packets-vp9]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ffmpeg-target-decoder]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x decoder_opened_packets_not_decoded_to_target_state`.
- Candidate family: `construct-and-seed-mutate`.
- Basin summary: The active verifier target was VP9 rather than the H.264 value visible in the build script.

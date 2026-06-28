---
type: causal-policy
title: "No Crash Vp7 Decoder Reached Clean Ffmpeg Vp7 Decoder Packet Stream Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal vp7_decoder_reached_clean."
failure_class: "no_crash"
verifier_signal: "vp7_decoder_reached_clean"
candidate_family: "construct"
input_format: "ffmpeg-vp7-decoder-packet-stream"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "vp7-decoder-reached-clean", "ffmpeg-vp7-decoder-packet-stream", "libfuzzer-ffmpeg-target-decoder", "negative-memory", "round-17"]
match_keys: ["no-crash", "vp7-decoder-reached-clean", "ffmpeg-vp7-decoder-packet-stream", "libfuzzer-ffmpeg-target-decoder", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Vp7 Decoder Reached Clean Ffmpeg Vp7 Decoder Packet Stream Negative Memory

- key: `no_crash x vp7_decoder_reached_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-vp7-decoder-packet-stream]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
- The initial hypotheses targeted a missing-slice video shape, but the actual verifier binary identified the fixed decoder as VP7 and decoded pixels cleanly.
- A productive next attempt should build a VP7 packet/frame stream with inconsistent partition or frame-dependency state rather than an HEVC-style access unit.

## Policy
Treat `no_crash x vp7_decoder_reached_clean` on `ffmpeg-vp7-decoder-packet-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `vp7_decoder_reached_clean`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[ffmpeg-vp7-decoder-packet-stream]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ffmpeg-target-decoder]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

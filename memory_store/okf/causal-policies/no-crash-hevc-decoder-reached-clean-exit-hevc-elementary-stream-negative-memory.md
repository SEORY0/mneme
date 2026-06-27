---
type: causal-policy
title: "No Crash Hevc Decoder Reached Clean Exit Hevc Elementary Stream Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal hevc_decoder_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "hevc_decoder_reached_clean_exit"
candidate_family: "construct"
input_format: "hevc-elementary-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "hevc-decoder-reached-clean-exit", "hevc-elementary-stream", "negative-memory", "round-12"]
match_keys: ["no_crash", "hevc_decoder_reached_clean_exit", "hevc-elementary-stream", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Hevc Decoder Reached Clean Exit Hevc Elementary Stream Negative Memory

- key: `no_crash x hevc_decoder_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[hevc-elementary-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
HEVC elementary-stream candidates reached the FFmpeg HEVC decoder and decoded pixels, including truncated and packet-split variants, but did not create the missing-slice condition that makes the fuzzer's non-zeroed buffers observable as uninitialized values.

## Policy
Treat `no_crash x hevc_decoder_reached_clean_exit` on `hevc-elementary-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The active target is the FFmpeg HEVC decoder fuzzer. The useful input is an HEVC elementary stream, optionally split by the target-decoder fuzz tag and optionally followed by a trailing codec-context block. Parameter sets and slice NAL units must be coherent enough for frame decoding.

## Harness Contract
The target_dec_fuzzer scans raw input for packet separators, opens a fixed decoder, optionally reads codec context fields and extradata from a trailing block when the input is large enough, and decodes packet by packet until exhaustion or an iteration cap.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `hevc_decoder_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

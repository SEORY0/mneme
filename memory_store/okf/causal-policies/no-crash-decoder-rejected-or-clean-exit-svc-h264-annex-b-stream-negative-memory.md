---
type: causal-policy
title: "No Crash Decoder Rejected Or Clean Exit Svc H264 Annex B Stream Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal decoder_rejected_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "decoder_rejected_or_clean_exit"
candidate_family: "construct"
input_format: "svc-h264-annex-b-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-rejected-or-clean-exit", "svc-h264-annex-b-stream", "negative-memory", "round-12"]
match_keys: ["no_crash", "decoder_rejected_or_clean_exit", "svc-h264-annex-b-stream", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Decoder Rejected Or Clean Exit Svc H264 Annex B Stream Negative Memory

- key: `no_crash x decoder_rejected_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[svc-h264-annex-b-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Small Annex-B style H.264/SVC probes exercised the svc decoder fuzzer controls and decode loop but did not create the required mismatch between decoder display dimensions and subset sequence dimensions.

## Policy
Treat `no_crash x decoder_rejected_or_clean_exit` on `svc-h264-annex-b-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The input is a raw H.264/SVC byte stream, commonly Annex-B NAL units, with the same bytes also used by the fuzzer for color format, core count, architecture, and target-layer selectors at fixed early positions. Valid SPS/PPS and slice structure are needed for meaningful header and frame decode.

## Harness Contract
The svc decoder fuzzer derives color format, core count, architecture, and target dependency layer from early input bytes, creates the decoder, decodes headers to establish output dimensions, allocates output frame buffers, then repeatedly decodes frames and reallocates when reported dimensions change.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_rejected_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

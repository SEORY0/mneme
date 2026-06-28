---
type: negative-memory
title: "No Crash Decoder Reached No Target Crash H264 Annex B Mvc Seed Mutate Heap Buffer Overflow Read Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal decoder_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "decoder_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "h264-annex-b-mvc"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-reached-no-target-crash", "h264-annex-b-mvc", "libfuzzer", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["no_crash", "decoder_reached_no_target_crash", "h264-annex-b-mvc", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Decoder Reached No Target Crash H264 Annex B Mvc Seed Mutate Heap Buffer Overflow Read Negative Memory

- key: `no_crash x decoder_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h264-annex-b-mvc]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid H.264 seeds and simple truncation/start-code-boundary mutations decoded cleanly in preserved candidate files. The target likely requires a specific CABAC 4x4 residual state, not just a generic short Annex-B slice.

## Policy
Treat `no_crash x decoder_reached_no_target_crash` on `h264-annex-b-mvc` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `decoder_reached_no_target_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is an H.264 Annex-B style byte stream for the MVC decoder. Start-code separated NAL units must include enough parameter-set and slice state to reach CABAC residual parsing; the target over-read occurs when slice data ends while NEXTBITS still reads ahead.

## Harness Contract
The MVC decoder fuzzer takes raw bytes, derives architecture/core/color controls from fixed positions when present, decodes headers, allocates output buffers, then repeatedly calls frame decode until data is consumed or decode fails.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 4 attempts.
- Scope: generator repair and basin avoidance only.

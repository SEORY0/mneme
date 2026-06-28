---
type: negative-memory
title: "No Crash Wtv Seed Clean Exit Ffmpeg Wtv Seed Replay Use Of Uninitialized Value Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal wtv_seed_clean_exit."
failure_class: "no_crash"
verifier_signal: "wtv_seed_clean_exit"
candidate_family: "seed_replay"
input_format: "ffmpeg-wtv"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wtv-seed-clean-exit", "ffmpeg-wtv", "libfuzzer", "seed-replay", "negative-memory", "round-25"]
match_keys: ["no_crash", "wtv_seed_clean_exit", "ffmpeg-wtv", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Wtv Seed Clean Exit Ffmpeg Wtv Seed Replay Use Of Uninitialized Value Negative Memory

- key: `no_crash x wtv_seed_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-wtv]]
- related harness facts: [[libfuzzer]]

## Failure Shape
An in-repo WTV sample parsed cleanly and did not reach the uninitialized descriptor buffer crash. The missing relation is a WTV event/stream table entry that causes the demuxer to call the MPEG-2 descriptor parser with a descriptor buffer whose declared length and initialized bytes diverge.

## Policy
Treat `no_crash x wtv_seed_clean_exit` on `ffmpeg-wtv` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `wtv_seed_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wtv_seed_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
WTV files are parsed through FFmpeg's WTV demuxer. The descriptor path is reached from WTV event entries associated with streams; descriptor bytes are copied into a local buffer and then parsed as MPEG-2 descriptors with tag and length fields.

## Harness Contract
The active libFuzzer binary is ffmpeg_dem_WTV_fuzzer. It feeds the whole file through a custom AVIO context to the WTV demuxer; there is no trailing filename/options envelope for this demuxer-specific build.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 1 attempt.
- Scope: generator repair and basin avoidance only.

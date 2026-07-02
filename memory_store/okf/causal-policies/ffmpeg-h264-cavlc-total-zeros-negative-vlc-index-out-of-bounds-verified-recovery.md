---
type: causal-policy
title: "FFmpeg H264 CAVLC Total Zeros Negative VLC Index Out Of Bounds Verified Recovery"
description: "Verified recovery for no_crash where H264 CAVLC decode_residual indexes a one-before-array VLC base, and the fix oracle needs a minimal single-coefficient block."
failure_class: "no_crash"
verifier_signal: "reached_cavlc_residual_one_before_array_index"
candidate_family: "seed_mutate"
input_format: "h264-annexb"
harness_convention: "ffmpeg-dec-fuzzer"
vuln_class: "out-of-bounds"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "seed-mutate", "h264-annexb", "out-of-bounds", "ubsan-negative-index", "verified-recovery"]
match_keys: ["no_crash", "reached_cavlc_residual_one_before_array_index", "h264-annexb", "ffmpeg-dec-fuzzer", "out-of-bounds", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# FFmpeg H264 CAVLC Total Zeros Negative VLC Index Out Of Bounds Verified Recovery

## Policy
For `no_crash` on the ffmpeg H264 decoder fuzzer (UBSan), the bug is in `decode_residual` (h264_cavlc.c):
the total-zeros VLC tables are indexed via a one-before-array base, `(total_zeros_vlc-1)[total_coeff]`, so a
`total_coeff` of 0 yields array index -1 (UBSan: array index -1 for type 'VLC[15]'). Reach CAVLC luma
residual decode of a single-coefficient block.

## Procedure
1. The harness is the ffmpeg dec fuzzer (FFMPEG_CODEC=H264); input is a raw H264 Annex-B elementary stream.
   Keep the file < 1024 bytes so the harness's trailing-1024-byte width/height override does not engage.
2. Build a minimal Baseline-CAVLC stream: SPS (type 7), PPS (type 8), IDR slice (type 5) with a slice header
   and the start of residual data for ONE luma block. Seed from a small conformance stream and truncate.
3. Brute-force single-byte mutations over the slice-data byte window; keep variants where the vul build
   aborts (UBSan) in decode_residual and the fix build exits 0.

## Format Contract
- See [[h264-annexb]]. Start-code-delimited NALs; CAVLC entropy mode (not CABAC) is required to hit the VLC
  table index.

## Negative Memory
- **fix-oracle trap:** a rich/normal H264 frame trips a SIBLING unpatched VLC bug elsewhere on BOTH builds,
  so fix_exit != 0 (over-broad → not a solve). Keep the stream MINIMAL (single-coefficient block) so ONLY
  the patched one-before-array index fires and the fix stays clean.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul abort, fix clean).

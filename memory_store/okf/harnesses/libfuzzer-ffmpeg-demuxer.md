---
type: harness-contract
title: "libfuzzer-ffmpeg-demuxer harness"
description: "Descriptive harness contract facts for libfuzzer-ffmpeg-demuxer."
tags: ["libfuzzer-ffmpeg-demuxer", "round-18"]
okf_support: 2
train_only: true
---
# Libfuzzer Ffmpeg Demuxer Harness

## Round 18 Input Contract

### Schema / Invariants
- The FFmpeg demuxer fuzzer feeds raw bytes through an AVIO buffer and lets probing select the demuxer from the stream signature when no filename tail is used. There is no FuzzedDataProvider split for this compact input; the whole file is the demuxer byte stream.

### Format Links
- [[vqf-twinvq]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 21 Input Contract (ffmpeg-ivr-realmedia-demuxer)

- The FFmpeg demuxer fuzzer builds an AVIOContext over raw input bytes. For this task the compiled target is ffmpeg_dem_IVR_fuzzer, not a generic RM fuzzer; raw bytes must be an IVR container and no leading selector is carved.

## Round 21 Format Links (ffmpeg-ivr-realmedia-demuxer)
- [[ffmpeg-ivr-realmedia-demuxer]]

## Round 21 Notes (ffmpeg-ivr-realmedia-demuxer)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

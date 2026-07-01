---
type: harness-contract
title: "Libfuzzer Ffmpeg Target Dec Fuzzer Harness"
description: "Round 26 input contract facts for libfuzzer-ffmpeg-target_dec_fuzzer."
tags: ["libfuzzer-ffmpeg-target-dec-fuzzer", "round-26"]
okf_support: 11
train_only: true
---
# Libfuzzer Ffmpeg Target Dec Fuzzer Harness

## Round 26 Factual Contract

### Input Contract
- FFmpeg target_dec_fuzzer treats the input prefix as decoder packet bytes for a fixed HEVC decoder. If the input is large enough, the last fixed-size context block can set parser, keyframe, flush, extradata, and codec context fields; otherwise the raw prefix is decoded directly. The harness can also split packets on its fixed separator tag, but the accepted candidate did not require a container or demuxer.

### Format Links
- [[hevc-elementary-stream]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 27 Input Contract
- The FFmpeg target decoder fuzzer feeds raw decoder packet bytes to the MLP decoder, not a demuxed media container.
- It scans for a fixed separator between packets; a separator-sized trailing region is needed when a single packet should be delivered in full.
- Inputs over the context-field threshold reserve the trailing context block for AVCodecContext fields.

## Round 27 Format Links
- [[ffmpeg-mlp-access-unit]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The FFmpeg target decoder libFuzzer harness feeds raw bytes directly to the compiled MLP decoder, with no demux container and no FuzzedDataProvider layout. It scans the input for a fixed packet separator; without an actual separator, a separator-sized trailing region is withheld from the packet, so a single full packet needs an inert tail of that size. The optional large-input codec-context trailer is not needed for this small audio packet.

### Format Links
- [[ffmpeg-mlp-access-unit]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

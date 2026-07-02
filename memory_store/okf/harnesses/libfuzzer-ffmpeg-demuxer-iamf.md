---
type: harness-contract
title: "Libfuzzer Ffmpeg Demuxer IAMF harness"
description: "Input contract facts for libfuzzer-ffmpeg-demuxer-iamf."
tags: ["libfuzzer-ffmpeg-demuxer-iamf", "round-20"]
okf_support: 1
---
# Libfuzzer Ffmpeg Demuxer IAMF Harness

## Round 20 Input Contract
- The active target is the FFmpeg IAMF demuxer fuzzer. It consumes the raw file bytes as a single IAMF bitstream; there is no external container, filename requirement, or fuzzer-side field carving.

## Round 20 Format Links
- [[iamf]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 28 Input Contract

- The FFmpeg demuxer fuzzer feeds raw bytes through an AVIOContext to the IAMF demuxer. With the IAMF demuxer selected, avformat_open_input and avformat_find_stream_info parse descriptors and then call av_read_frame/ff_iamf_read_packet. The packet reader reads a fixed-size OBU header window from the current stream position and passes that stack buffer to the IAMF OBU header parser.

## Round 28 Format Links
- [[iamf]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

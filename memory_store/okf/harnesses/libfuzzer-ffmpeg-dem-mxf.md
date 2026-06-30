---
type: harness-contract
title: "Libfuzzer Ffmpeg Dem Mxf Harness"
description: "Input contract facts for libfuzzer-ffmpeg-dem-mxf."
tags: ["libfuzzer-ffmpeg-dem-mxf", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Ffmpeg Dem Mxf Harness

## Round 30 Input Contract

### Input Contract
- The FFmpeg MXF demuxer fuzzer feeds the input through a synthetic AVIO stream to the MXF demuxer. Small inputs are used as raw MXF bytes. Larger inputs reserve a trailing fuzzer-control block for IO options such as seekability and virtual file size; those control bytes are not part of the media content.

### Format Links
- [[mxf]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

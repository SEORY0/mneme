---
type: harness-contract
title: "oss-fuzz-run_poc-ffmpeg-target-decoder harness"
description: "Descriptive harness contract facts for oss-fuzz-run_poc-ffmpeg-target-decoder."
tags: ["oss-fuzz-run-poc-ffmpeg-target-decoder", "round-18"]
okf_support: 10
train_only: true
---
# Oss Fuzz Run Poc Ffmpeg Target Decoder Harness

## Round 18 Input Contract

### Schema / Invariants
- The oss-fuzz `run_poc` wrapper invokes the compiled `ffmpeg_AV_CODEC_ID_RV40_fuzzer`. The target_dec_fuzzer treats the entire file as packet bytes and repeatedly parses/decodes packets; there is no archive envelope, mode byte, or FuzzedDataProvider layout.

### Format Links
- [[ffmpeg-rv40-decoder-packet]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 19 Input Contract

- The OSS-Fuzz run_poc wrapper invokes the generated FFmpeg target decoder fuzzer on the PoC file. The decoder fuzzer consumes the file as packet bytes for one compiled decoder, can split packets internally, and may use a trailing context block on larger inputs. There is no front mode byte and no FuzzedDataProvider object.
- Format link: [[ffmpeg-mpegvideo-target-decoder-packets]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 27 Input Contract
- The run_poc wrapper invokes the generated FFmpeg RV30 target-decoder fuzzer.
- The input is a sequence of raw decoder packets separated by the target fuzzer's fixed packet tag, followed by decoder extradata and a final control footer for context fields.
- The footer supplies dimensions, parser selection, keyframe flags, flush behavior, and extradata; there is no archive envelope and no FuzzedDataProvider front/back layout.

## Round 27 Format Links
- [[ffmpeg-rv30-target-decoder-packets]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 29 Input Contract

- The OSS-Fuzz run_poc wrapper invokes the compiled FFmpeg AIC target-decoder fuzzer. The input is raw decoder packet data; for larger inputs the final fixed-size configuration block can set codec-context fields such as dimensions and parser flags. There is no demuxer container requirement, front selector byte, or FuzzedDataProvider split.
- The generated run_poc wrapper invokes the FFmpeg VP7 target-decoder fuzzer on the PoC file. The fuzzer treats bytes as decoder packets, optionally split by its fixed packet separator, and for larger inputs reads a fixed-size control area for codec context, parser, keyframe, flush, and extradata settings. There is no FuzzedDataProvider front/back layout and no demuxer stage in the wrapper.

## Round 29 Format Links
- [[ffmpeg-aic-target-decoder-packet]]
- [[ffmpeg-vp7-target-decoder-packets]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 30 Input Contract

### Input Contract
- The OSS-Fuzz FFmpeg target-decoder wrapper passes raw packet bytes to the compiled AIC decoder. When the input is large enough, a final fixed-size trailer is consumed as codec-context configuration, including dimensions and parser flags, and is removed from the packet data. There is no demuxer container, no leading selector byte, and no FuzzedDataProvider field carving.

### Format Links
- [[ffmpeg-aic-target-decoder-packet]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

---
type: harness-contract
title: "Libfuzzer Ffmpeg Target Decoder harness"
description: "Input contract facts for libfuzzer-ffmpeg-target-decoder."
tags: ["libfuzzer-ffmpeg-target-decoder", "round-11"]
okf_support: 8
train_only: true
---
# Libfuzzer Ffmpeg Target Decoder Harness

## Round 11 Input Contract
- The libFuzzer target receives raw bytes and routes them to the target decoder for the selected codec. No file container is required, and no front mode byte is used for this task; optional context configuration is taken from the tail of sufficiently large inputs.

## Format Links
- [[ffmpeg-hevc-target-decoder-frame]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 13 Facts
- The FFmpeg targeted decoder harness passes raw bytes to the H.264 decoder as one or more packets. A fixed internal separator can split multiple packets. If the input is large enough, the tail is consumed as codec-context configuration and removed from packet data before decoding.
- The FFmpeg target decoder fuzzer runs a fixed decoder on the raw input file, optionally through FFmpeg parser logic, with no outer container required and no FuzzedDataProvider fields in front of the codec bytes.

## Round 17 Input Contract
- The OSS-Fuzz local verifier runs the generated libFuzzer target on the PoC file via the standard run_poc path.
- The PoC is a raw decoder input, not a FuzzedDataProvider stream with front/back field consumption.

## Round 17 Format Links
- [[ffmpeg-vp7-decoder-packet-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[ffmpeg-vp7-decoder-packet-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 18 Input Contract

### Schema / Invariants
- FFmpeg target_dec_fuzzer treats the leading data as one or more raw packets separated by an internal tag. If the input is large enough, a fixed-size trailer is consumed as codec-context configuration such as width, height, flags, and optional extradata.
- The FFmpeg target decoder fuzzer initializes one compiled decoder, assigns a custom get_buffer2 callback for video, optionally consumes a configuration tail from the end of inputs larger than the threshold, then splits the remaining front bytes into packets on the fixed tag. It may initialize a parser based on a tail flag; otherwise packets are sent directly to avcodec_send_packet and avcodec_receive_frame.
- FFmpeg target_dec_fuzzer feeds raw packets directly to the selected decoder, optionally using a fixed-size trailer as codec-context configuration. Without the trailer, the packet itself must provide dimensions accepted by the decoder.

### Format Links
- [[ffmpeg-target-decoder-frame]]
- [[ffmpeg-target-decoder-packets-vp9]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 20 Input Contract
- The FFmpeg target-decoder libFuzzer harness consumes raw file bytes as one or more packets separated by the harness packet delimiter. An optional trailing configuration block can set codec context fields for large inputs; this CLUT path did not require it. Local verify may classify the sanitizer report as wrong_sink even when the described parser function is reached.
- The FFmpeg target-decoder harness consumes raw decoder packets separated by a fixed delimiter and can optionally consume a trailing codec-context configuration block for large inputs. It does not demux RealMedia containers; demuxed RV60 packet payloads are needed for reliable reachability.
- The FFmpeg target-decoder harness is an elementary decoder harness. It splits input into packets by the harness delimiter and may use a trailing context-configuration block; it does not demux AVI containers before calling the FFV1 decoder.

## Round 20 Format Links
- [[ffmpeg-dvbsub-packet-stream]]
- [[ffmpeg-ffv1-elementary-packet-stream]]
- [[ffmpeg-rv60-elementary-packet-stream]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 24 Factual Contract

### Input Contract
- If the input exceeds the trailer threshold, the final trailer configures codec context fields such as dimensions, flags, parser use, extradata length, sample/channel fields, keyframe flags, flush pattern, and debug/workaround flags. The fuzzer then opens the codec, optionally parses packets, sends them to the decoder, and drains frames while reporting decoded pixels.

### Format Links
- [[ffmpeg-target-decoder-vp6f]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 29 Input Contract

- The FFmpeg target decoder fuzzer feeds the selected decoder with raw packet bytes. The input may contain an optional fixed delimiter that splits multiple packets, but no demux container is parsed. Very large inputs may also provide trailing codec-context fields; ordinary small inputs are treated as direct packet data.

## Round 29 Format Links
- [[ac3-eac3-audio-frame]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 30 Input Contract

### Input Contract
- The FFmpeg target decoder libFuzzer harness feeds the input as raw HEVC decoder packet bytes for a fixed HEVC decoder. For small inputs, the whole file is decoded directly; larger inputs may reserve a trailing codec-context block and packet separators may be recognized, but this carrier does not need a media container, filename wrapper, or FuzzedDataProvider layout.
- OSS-Fuzz run_poc invokes the compiled FFmpeg target decoder fuzzer. Raw prefix bytes are packet data and may be split into packets by a fixed fuzzer tag. For inputs over the trailer threshold, the final fixed-size control tail configures parser flags, error-recognition behavior, keyframe and flush patterns, skip-frame behavior, and an extradata size. Extradata is copied from immediately before that tail and removed from the packet prefix. There is no FuzzedDataProvider front/back stream.

### Format Links
- [[hevc-annex-b-elementary-stream]]
- [[vc1-elementary-stream]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The FFmpeg target decoder harness feeds the file bytes as raw packet data for the selected decoder. It may split tagged multi-packet inputs, but this task can be reached with a single raw packet and does not use FuzzedDataProvider front/back carving. The container wrapper consumes the mounted poc path implicitly.
- The FFmpeg target decoder fuzzer feeds raw packet bytes to a fixed AC3 decoder target. It may split packets on an internal delimiter and may reserve a large trailing context block for codec fields on large inputs, but ordinary small inputs are decoded directly as packet payloads. There is no demux container, filename wrapper, or FuzzedDataProvider front/back carving.
- The FFmpeg decoder libFuzzer harness passes the file bytes directly to the selected H.264 decoder as packet data. There is no FuzzedDataProvider prefix or mode byte. A fixed packet delimiter can split multiple packets, and inputs above the harness threshold reserve a trailing codec-context configuration block, so the successful family kept the candidate compact.

### Format Links
- [[ac3-eac3-audio-frame]]
- [[ffmpeg-mimic-decoder-packet]]
- [[h264-annex-b]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

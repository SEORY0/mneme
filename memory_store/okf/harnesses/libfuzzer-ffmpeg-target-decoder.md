---
type: harness
title: "Libfuzzer Ffmpeg Target Decoder"
harness_convention: libfuzzer-ffmpeg-target-decoder
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Ffmpeg Target Decoder

## Input Contract
- For `h264-annexb-or-target-decoder-packet`, The FFmpeg targeted decoder harness passes raw bytes to the H.264 decoder as one or more packets. A fixed internal separator can split multiple packets. If the input is large enough, the tail is consumed as codec-context configuration and removed from packet data before decoding.
- For `vc1image-elementary-stream`, The FFmpeg target decoder fuzzer runs a fixed decoder on the raw input file, optionally through FFmpeg parser logic, with no outer container required and no FuzzedDataProvider fields in front of the codec bytes.

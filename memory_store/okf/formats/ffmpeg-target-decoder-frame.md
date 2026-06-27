---
type: format
title: "Ffmpeg Target Decoder Frame"
input_format: ffmpeg-target-decoder-frame
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Ffmpeg Target Decoder Frame

## Schema
- The FFmpeg target decoder fuzzer treats the front of the input as one or more raw packet regions separated by a fixed split tag. When the input is large enough, a fixed-size tail configures codec context fields and optional extradata before avcodec_open2 and packet decoding.

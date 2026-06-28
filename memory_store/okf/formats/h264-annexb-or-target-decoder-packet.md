---
type: format
title: "H264 Annexb Or Target Decoder Packet"
access_scope: generate
confidence: medium
tags: ["h264-annexb-or-target-decoder-packet", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# H264 Annexb Or Target Decoder Packet

## Round 13 Facts
- The target format is raw H.264 decoder packet data. Parser reachability requires recognizable parameter-set NAL units before slice data; CAVLC behavior depends on slice syntax, entropy mode, residual block type, coefficient counts, total-zero coding, and run-before coding.

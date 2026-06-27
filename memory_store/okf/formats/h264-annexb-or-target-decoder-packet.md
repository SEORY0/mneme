---
type: format
title: "H264 Annexb Or Target Decoder Packet"
input_format: h264-annexb-or-target-decoder-packet
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# H264 Annexb Or Target Decoder Packet

## Schema
- The target format is raw H.264 decoder packet data. Parser reachability requires recognizable parameter-set NAL units before slice data; CAVLC behavior depends on slice syntax, entropy mode, residual block type, coefficient counts, total-zero coding, and run-before coding.

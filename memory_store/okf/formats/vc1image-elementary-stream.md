---
type: format
title: "Vc1image Elementary Stream"
access_scope: generate
confidence: medium
tags: ["vc1image-elementary-stream", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Vc1image Elementary Stream

## Round 13 Facts
- The target consumes raw VC1-family decoder payloads rather than a media container. The active binary is the VC1IMAGE decoder fuzzer; ordinary VC1/RCV elementary streams can be accepted but may not drive the exact image-coded macroblock path tied to the uninitialized mb_type and transform-type tables.

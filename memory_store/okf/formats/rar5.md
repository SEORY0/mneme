---
type: format
title: Rar5
input_format: rar5
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Rar5

## Schema
- RAR5 inputs start with the RAR5 marker, then CRC-protected variable-length base block headers. FILE base blocks carry split-before/split-after flags, data size, unpacked size, compression metadata, and a dictionary/window-size selector; header CRC validity is a hard parser gate.

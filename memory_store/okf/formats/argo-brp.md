---
type: format
title: "Argo Brp"
access_scope: generate
confidence: medium
tags: ["argo-brp", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Argo Brp

## Round 13 Facts
- Argonaut BRP starts with a small little-endian file header containing the BRP magic, stream count, and byte rate, followed by one fixed-size stream header per stream. A BASF stream header uses an embedded ASF file header as extradata; that ASF header must have the ASF magic, a nonzero chunk count, and a chunk offset at least as large as the ASF file header. BRP media blocks then use a fixed-size block header with stream id, timestamp, and block size. BASF blocks begin with an ASF chunk header containing block count, sample count, sample rate, flags, and related fields; accepted chunk headers need the expected sample count and standard flags before audio packet timing is derived from them.

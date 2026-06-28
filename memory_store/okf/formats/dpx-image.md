---
type: format
title: "Dpx Image"
access_scope: generate
confidence: medium
tags: ["dpx-image", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Dpx Image

## Round 13 Facts
- DPX files begin with a DPX magic and fixed-size headers describing pixel-data offset, image dimensions, element count, and per-element descriptors. ColorDifferenceCbCr elements are handled by a subsampled chroma path; the relevant validation relation is odd image width versus descriptor family.

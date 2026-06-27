---
type: format
title: "Dpx Image"
input_format: dpx-image
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Dpx Image

## Schema
- DPX files begin with a DPX magic and fixed-size headers describing pixel-data offset, image dimensions, element count, and per-element descriptors. ColorDifferenceCbCr elements are handled by a subsampled chroma path; the relevant validation relation is odd image width versus descriptor family.

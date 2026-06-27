---
type: harness
title: "Libfuzzer Whole Buffer Frame Decompressor"
access_scope: generate
confidence: medium
tags: ["libfuzzer-whole-buffer-frame-decompressor", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Whole Buffer Frame Decompressor

## Round 13 Facts
- The fuzzer feeds the whole PoC buffer directly to blosc2_schunk_from_buffer. If the frame opens, it allocates a destination from the declared uncompressed byte count and attempts chunk decompression. There is no selector byte, filename wrapper, checksum recomputation requirement, or FuzzedDataProvider carving.

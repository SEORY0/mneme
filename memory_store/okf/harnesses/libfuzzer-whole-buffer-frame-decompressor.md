---
type: harness
title: "Libfuzzer Whole Buffer Frame Decompressor"
harness_convention: "libfuzzer whole-buffer frame decompressor"
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Whole Buffer Frame Decompressor

## Input Contract
- For `c-blosc2-frame`, The fuzzer feeds the whole PoC buffer directly to blosc2_schunk_from_buffer. If the frame opens, it allocates a destination from the declared uncompressed byte count and attempts chunk decompression. There is no selector byte, filename wrapper, checksum recomputation requirement, or FuzzedDataProvider carving.

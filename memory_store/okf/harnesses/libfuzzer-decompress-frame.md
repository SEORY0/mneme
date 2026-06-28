---
type: harness
title: "Libfuzzer Decompress Frame"
access_scope: generate
confidence: medium
tags: ["libfuzzer-decompress-frame", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Decompress Frame

## Round 13 Facts
- The libFuzzer decompress-frame target passes the whole raw input to blosc2_schunk_open_sframe. If frame reconstruction succeeds, it allocates an output buffer from the parsed uncompressed size, attempts chunk decompression, then frees the reconstructed super-chunk. There is no leading selector byte or FuzzedDataProvider carving.

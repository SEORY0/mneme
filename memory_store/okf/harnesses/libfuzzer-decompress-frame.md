---
type: harness
title: "Libfuzzer Decompress Frame"
harness_convention: libfuzzer-decompress-frame
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Decompress Frame

## Input Contract
- For `c-blosc2-frame`, The libFuzzer decompress-frame target passes the whole raw input to blosc2_schunk_open_sframe. If frame reconstruction succeeds, it allocates an output buffer from the parsed uncompressed size, attempts chunk decompression, then frees the reconstructed super-chunk. There is no leading selector byte or FuzzedDataProvider carving.

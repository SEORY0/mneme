---
type: harness
title: "Honggfuzz Libfuzzer Style Raw Bytes To Simple Compress"
harness_convention: "honggfuzz/libfuzzer-style raw bytes to simple_compress"
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Honggfuzz Libfuzzer Style Raw Bytes To Simple Compress

## Input Contract
- For `zstd-simple-compress-fuzzer-bytes`, The target creates a FUZZ_dataProducer over the whole input, consumes bytes from the back to choose how much of the front remains as source data, then consumes more back bytes to choose destination capacity and compression level. It calls ZSTD_compressCCtx and accepts only dstSize_tooSmall as an expected error. There is no checksum, file wrapper, or FuzzedDataProvider object beyond this back-consuming suffix contract.

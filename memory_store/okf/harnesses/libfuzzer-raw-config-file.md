---
type: harness
title: "Libfuzzer Raw Config File"
harness_convention: libfuzzer-raw-config-file
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Raw Config File

## Input Contract
- For `haproxy-config`, The fuzzer writes the raw input bytes to a temporary config file and calls readcfgfile directly when the file is large enough. There is no mode byte, checksum, or secondary file contract.

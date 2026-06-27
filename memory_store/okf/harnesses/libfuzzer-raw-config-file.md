---
type: harness
title: "Libfuzzer Raw Config File"
access_scope: generate
confidence: medium
tags: ["libfuzzer-raw-config-file", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Raw Config File

## Round 13 Facts
- The fuzzer writes the raw input bytes to a temporary config file and calls readcfgfile directly when the file is large enough. There is no mode byte, checksum, or secondary file contract.

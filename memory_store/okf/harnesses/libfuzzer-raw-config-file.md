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

## Round 27 Input Contract
- The libFuzzer harness feeds raw file bytes.
- It rejects only very small inputs, writes the remaining bytes unchanged to a temporary config file, invokes readcfgfile on that file, and uses no mode selector, integrity field, FuzzedDataProvider tail fields, or secondary resource.

## Round 27 Format Links
- [[haproxy-config]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

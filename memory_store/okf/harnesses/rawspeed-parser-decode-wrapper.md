---
type: harness
title: "Rawspeed Parser Decode Wrapper"
access_scope: generate
confidence: medium
tags: ["rawspeed-parser-decode-wrapper", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Rawspeed Parser Decode Wrapper

## Round 13 Facts
- The selected RawSpeed wrapper passes the raw file bytes to a RawParser/GetDecoder/Decode flow. It is not a FuzzedDataProvider layout; malformed or empty inputs can fail in wrapper/parser setup before any decoder-specific Samsung logic is reached.

---
type: harness
title: "Rawspeed Parser Decode Wrapper"
harness_convention: rawspeed-parser-decode-wrapper
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Rawspeed Parser Decode Wrapper

## Input Contract
- For `samsung-srw-tiff`, The selected RawSpeed wrapper passes the raw file bytes to a RawParser/GetDecoder/Decode flow. It is not a FuzzedDataProvider layout; malformed or empty inputs can fail in wrapper/parser setup before any decoder-specific Samsung logic is reached.

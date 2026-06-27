---
type: harness
title: "Libfuzzer Whole Buffer Libraw"
access_scope: generate
confidence: medium
tags: ["libfuzzer-whole-buffer-libraw", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Whole Buffer Libraw

## Round 13 Facts
- The fuzzer passes the entire PoC buffer to LibRaw open_buffer, then would call unpack and dcraw_process only if opening succeeds. There is no leading selector, checksum, path argument, or FuzzedDataProvider carving; the file signature selects the parser path.

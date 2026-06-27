---
type: harness
title: "Libfuzzer Whole Buffer Libraw"
harness_convention: "libfuzzer whole-buffer LibRaw"
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Whole Buffer Libraw

## Input Contract
- For `rollei-raw-text-header`, The fuzzer passes the entire PoC buffer to LibRaw open_buffer, then would call unpack and dcraw_process only if opening succeeds. There is no leading selector, checksum, path argument, or FuzzedDataProvider carving; the file signature selects the parser path.

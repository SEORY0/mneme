---
type: harness
title: "Libfuzzer Mruby Load String"
harness_convention: libfuzzer-mruby-load-string
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Mruby Load String

## Input Contract
- For `mruby-script`, The mruby harness copies raw bytes into a NUL-terminated string, opens a fresh mruby state, calls mrb_load_string, then closes the state. There is no prefix, length field, or FuzzedDataProvider layout.
- For `mruby-script`, The OSS-Fuzz mruby harness copies the raw bytes into a NUL-terminated code buffer, opens a new mruby state, evaluates the code string, and closes the state. There is no byte-level carving or external file contract.

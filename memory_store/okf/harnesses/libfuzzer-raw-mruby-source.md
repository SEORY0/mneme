---
type: harness
title: "Libfuzzer Raw Mruby Source"
harness_convention: "libfuzzer raw mruby source"
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Raw Mruby Source

## Input Contract
- For `mruby-script`, The fuzzer passes the whole file as mruby source to the mruby_fuzzer target. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving. Syntax must compile far enough for the VM to execute the literal load path.

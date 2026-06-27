---
type: harness
title: "Libfuzzer Raw Mruby Source"
access_scope: generate
confidence: medium
tags: ["libfuzzer-raw-mruby-source", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Raw Mruby Source

## Round 13 Facts
- The fuzzer passes the whole file as mruby source to the mruby_fuzzer target. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving. Syntax must compile far enough for the VM to execute the literal load path.

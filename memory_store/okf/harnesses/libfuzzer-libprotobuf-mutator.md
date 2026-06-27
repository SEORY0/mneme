---
type: harness
title: "Libfuzzer Libprotobuf Mutator"
harness_convention: libfuzzer-libprotobuf-mutator
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Libprotobuf Mutator

## Input Contract
- For `protobuf-text-to-mruby-source`, The build contains a raw mruby string harness and a libprotobuf-mutator harness. The verifier selected the protobuf harness, which parses the input as a Function message, converts it to Ruby source, then passes the generated source to mrb_load_string. Arbitrary Ruby source is not accepted on this target path.

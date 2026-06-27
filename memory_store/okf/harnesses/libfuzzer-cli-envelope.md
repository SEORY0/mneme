---
type: harness
title: "Libfuzzer Cli Envelope"
harness_convention: libfuzzer-cli-envelope
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Cli Envelope

## Input Contract
- For `metaflac-cli-fuzzer-envelope-with-cuesheet`, The selected target is a metaflac CLI fuzzer. The first byte controls maximum argument count and whether stdin is used; NUL-delimited strings become command-line arguments. Remaining bytes are split into a temporary FLAC file and, when stdin mode is selected, a temporary stdin stream.

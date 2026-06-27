---
type: harness
title: "Libfuzzer Cli Envelope"
access_scope: generate
confidence: medium
tags: ["libfuzzer-cli-envelope", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Cli Envelope

## Round 13 Facts
- The selected target is a metaflac CLI fuzzer. The first byte controls maximum argument count and whether stdin is used; NUL-delimited strings become command-line arguments. Remaining bytes are split into a temporary FLAC file and, when stdin mode is selected, a temporary stdin stream.

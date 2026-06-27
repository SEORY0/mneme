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

## Round 15 Input Contract
- The first input byte controls the maximum number of NUL-delimited argv strings and whether stdin
  mode is used. In stdin mode the remaining bytes after argv are split in half: the first half is
  written to the temporary FLAC file and the second half is used as stdin. Without stdin mode the same
  temporary filename is appended twice to argv.

## Format Links
- [[metaflac-cli-envelope-with-flac-and-cuesheet]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

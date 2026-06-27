---
type: harness
title: "Honggfuzz File"
harness_convention: honggfuzz-file
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Honggfuzz File

## Input Contract
- For `bfd-archive-vms-object`, The source fuzzer writes raw input to a temporary file, opens it with BFD auto-detection, and calls archive-format checking. The arvo image wrapper for this task appears to be honggfuzz-oriented and did not produce the normal one-input libFuzzer execution transcript.

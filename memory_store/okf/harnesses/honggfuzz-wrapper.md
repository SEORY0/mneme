---
type: harness
title: "Honggfuzz Wrapper"
harness_convention: honggfuzz-wrapper
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Honggfuzz Wrapper

## Input Contract
- For `openthread-ip6-send-or-meshcop-tlv`, The source tree builds OpenThread fuzz targets including ip6-send, radio-receive-done, ncp-uart-received, and cli-uart-received. Local verify identified the selected target as the ip6-send honggfuzz wrapper; the wrapper printed fuzzing usage instead of consuming the supplied single PoC file as raw input.

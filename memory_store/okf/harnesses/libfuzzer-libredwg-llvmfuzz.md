---
type: harness
title: "Libfuzzer Libredwg Llvmfuzz"
access_scope: generate
confidence: medium
tags: ["libfuzzer-libredwg-llvmfuzz", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Libredwg Llvmfuzz

## Round 13 Facts
- The llvmfuzz target copies and null-terminates text-like inputs, imports DWG, JSON, or DXF into a Dwg_Data object, chooses one output path from the enabled encoders using the process PRNG, writes to a null sink, then frees the Dwg_Data. PoC reachability therefore includes both import cleanup and the selected export cleanup path.

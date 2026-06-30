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

## Round 30 Input Contract

### Input Contract
- The libFuzzer harness consumes the file bytes directly with no mode prefix or FuzzedDataProvider carving. LibreDWG dispatches by leading content: DWG-like buffers by signature, JSON-like buffers by an opening brace, and otherwise DXF text. The harness imports the document, writes a derived representation to a null sink, then frees the document, so cleanup-time object corruption is observable.

### Format Links
- [[dxf]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

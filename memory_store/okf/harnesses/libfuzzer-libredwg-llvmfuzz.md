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

## Round 38 Factual Contract

### Input Contract
- The libFuzzer target consumes the file as raw bytes with no FuzzedDataProvider carving. It dispatches by leading content, copies and appends a terminator for text-like inputs only when the original input does not already end in an accepted terminator, imports the drawing, may export to a null sink, and then frees the drawing state.
- The llvmfuzz harness consumes the raw file bytes directly with no mode byte and no FuzzedDataProvider carving. Buffers beginning with a DWG signature take the binary DWG decoder, buffers beginning with a JSON object take the JSON reader, and other text is routed to the DXF reader. After import, the harness may write one derived output format to a null sink and then frees the drawing, so parser, writer, and cleanup paths can all be relevant.

### Format Links
- [[dxf-text]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

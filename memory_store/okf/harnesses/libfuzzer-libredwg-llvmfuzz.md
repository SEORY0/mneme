---
type: harness
title: "Libfuzzer Libredwg Llvmfuzz"
harness_convention: libfuzzer-libredwg-llvmfuzz
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Libredwg Llvmfuzz

## Input Contract
- For `dxf-or-json-cad`, The llvmfuzz target copies and null-terminates text-like inputs, imports DWG, JSON, or DXF into a Dwg_Data object, chooses one output path from the enabled encoders using the process PRNG, writes to a null sink, then frees the Dwg_Data. PoC reachability therefore includes both import cleanup and the selected export cleanup path.

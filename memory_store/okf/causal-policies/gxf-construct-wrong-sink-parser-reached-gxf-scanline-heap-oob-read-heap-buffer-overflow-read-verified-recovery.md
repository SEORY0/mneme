---
type: causal-policy
title: "Gxf Construct Wrong Sink Parser Reached Gxf Scanline Heap Oob Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for gxf when wrong_sink pairs with parser_reached_gxf_scanline_heap_oob_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_gxf_scanline_heap_oob_read"
candidate_family: "construct"
input_format: "gxf"
harness_convention: "libfuzzer-filesystem-gdal-raster-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-gxf-scanline-heap-oob-read", "gxf", "libfuzzer-filesystem-gdal-raster-fuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-gxf-scanline-heap-oob-read", "gxf", "libfuzzer-filesystem-gdal-raster-fuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Gxf Construct Wrong Sink Parser Reached Gxf Scanline Heap Oob Read Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_gxf_scanline_heap_oob_read`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[gxf]]
- related harness facts: [[libfuzzer-filesystem-gdal-raster-fuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_gxf_scanline_heap_oob_read`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[gxf]]
- related harness facts: [[libfuzzer-filesystem-gdal-raster-fuzzer]]

### Policy
When `wrong_sink x parser_reached_gxf_scanline_heap_oob_read` appears for `gxf`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-filesystem-gdal-raster-fuzzer]] harness contract and the [[gxf]] format contract before changing sink fields.
2. Recreate the verified causal relation: Build a minimal but recognizable ASCII GXF grid: include enough header content for GDAL's GXF recognizer, valid point and row dimensions, the compressed-token width field, and a grid section with at least one data line. Set the compressed-token width field to an invalid negative value while leaving the rest of the grid structurally plausible. The vulnerable scanline reader enters the compressed path, skips the short-line rejection, and moves its token pointer before the current line buffer; the fixed build rejects the invalid width.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
GXF is an ASCII grid format with hash-prefixed header sections for point count, row count, optional metadata and transforms, an optional compressed-token width field, and a grid section. In compressed grids, the token-width field controls how many characters are consumed for each encoded numeric token while scanlines are expanded.

### Harness Contract
The GDAL raster libFuzzer wrapper treats the PoC as a raw file, stores it as a temporary or virtual dataset, calls GDALOpen, and then computes raster checksums. Parser reachability depends on the file being self-identifying enough for the GXF driver before checksum-driven band reads call the GXF scanline decoder.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_gxf_scanline_heap_oob_read`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

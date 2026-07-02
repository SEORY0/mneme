---
type: causal-policy
title: "Pdf Construct Wrong Sink Parser Reached Heap Buffer Overflow Write Heap Buffer Overflow Write Verified Recovery"
description: "Server-verified recovery for pdf when wrong_sink pairs with parser_reached_heap_buffer_overflow_write."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_heap_buffer_overflow_write"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-mupdf-pdf-render"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-heap-buffer-overflow-write", "pdf", "libfuzzer-mupdf-pdf-render", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-heap-buffer-overflow-write", "pdf", "libfuzzer-mupdf-pdf-render", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Pdf Construct Wrong Sink Parser Reached Heap Buffer Overflow Write Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_heap_buffer_overflow_write`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer-mupdf-pdf-render]]

## Policy
When `wrong_sink x parser_reached_heap_buffer_overflow_write` appears for `pdf`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-mupdf-pdf-render` harness contract and the `pdf` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Build a complete renderable PDF page whose resources invoke function-based shading. Use a parent stitching function whose advertised output arity matches the color space, but make the selected subfunction advertise more outputs than the parent. Rendering evaluates the subfunction through the parent-sized output buffer, so the vulnerable build writes past that buffer while the fixed build rejects or clamps the mismatch.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[pdf]]. PDF rendering needs a valid catalog, page tree, page, content stream, and resource dictionary. A shading resource can trigger Type 3 stitching functions during page painting. Function output arity is derived from Range entries, and subfunctions may have independent arity unless the parser enforces consistency.

## Harness Contract
Use [[libfuzzer-mupdf-pdf-render]]. The libFuzzer input is used directly as PDF bytes in memory. The harness opens the document and renders pages; there is no leading mode byte, carved section, checksum wrapper, or FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_heap_buffer_overflow_write`.
- Vulnerability class: `heap-buffer-overflow-write`.
- Recovery summary: Build a complete renderable PDF page whose resources invoke function-based shading. Use a parent stitching function whose advertised output arity matches the color space, but make the selected subfunction advertise more outputs than the parent. Rendering evaluates the subfunction through the parent-sized output buffer, so the vulnerable build writes past that buffer while the fixed build rejects or clamps the mismatch.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

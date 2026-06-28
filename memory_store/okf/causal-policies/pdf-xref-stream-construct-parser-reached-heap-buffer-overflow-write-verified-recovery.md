---
type: causal-policy
title: "PDF Xref Stream Construct Parser Reached Heap Buffer Overflow Write Verified Recovery"
description: "Round 16 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "pdf-xref-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "pdf-xref-stream", "construct", "verified-recovery", "round-16"]
match_keys: ["generic_crash", "parser_reached", "pdf-xref-stream", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 16
---
# PDF Xref Stream Construct Parser Reached Heap Buffer Overflow Write Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
- Build a minimal valid PDF with a normal catalog/page skeleton and two cross-reference streams. Make the newer xref stream the start target with a small table size and a previous-xref pointer to an older xref stream whose declared table size is larger. Keep both streams syntactically valid and unfiltered so the parser allocates from the first size, follows the previous pointer, and then processes more entries than the initial table can hold.
- Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
- If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- PDF xref streams are indirect stream objects with Type XRef, Size, W field-width array, optional Index, and trailer keys such as Root and Prev. The startxref marker points to the active xref stream; a Prev key chains to an older xref section or stream.
- Harness: The Ghostscript raster fuzzer passes raw stdin bytes to gsapi with a cups raster output device. There is no fuzzer envelope; a valid enough PDF header, objects, xref stream, startxref, and EOF marker are required for the PDF interpreter to reach xref processing.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-16 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

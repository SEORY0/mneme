---
type: causal-policy
title: "PDF Xref Stream Construct Parser Reached Compressed Xref Dereference Null Dereference From Xref Off By One Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached_compressed_xref_dereference."
failure_class: "generic_crash"
verifier_signal: "parser_reached_compressed_xref_dereference"
candidate_family: "construct"
input_format: "pdf-xref-stream"
harness_convention: "libfuzzer"
vuln_class: "null-dereference-from-xref-off-by-one"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-compressed-xref-dereference", "pdf-xref-stream", "libfuzzer", "construct", "null-dereference-from-xref-off-by-one", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached_compressed_xref_dereference", "pdf-xref-stream", "libfuzzer", "null-dereference-from-xref-off-by-one", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# PDF Xref Stream Construct Parser Reached Compressed Xref Dereference Null Dereference From Xref Off By One Verified Recovery

## Policy
For `generic_crash x parser_reached_compressed_xref_dereference`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal PDF with a coherent xref stream trailer and make the document root reference an object whose xref entry is a compressed-object entry.
2. Keep the xref stream dictionary, stream length, width table, and startxref relation self-consistent, but set the compressed-object stream reference to the first value just outside the declared xref table capacity.
3. This reaches compressed-object dereference with an out-of-range object-stream index while the rest of the PDF remains parseable.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A PDF xref stream is an indirect stream with an xref dictionary containing trailer keys, a declared table size, a field-width array, and optionally index ranges.
- Stream records encode free, uncompressed, and compressed-object entries; compressed-object records name an object stream plus an index within that stream.
- The parser follows startxref to the xref stream before resolving the root object.
- Harness [[libfuzzer]]:
  - The Ghostscript gstoraster fuzzer feeds the raw input bytes as a document on stdin.
  - There is no carved selector or FuzzedDataProvider layout; parser reachability depends on PDF syntax, startxref, and xref-stream consistency.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[pdf-xref-stream]] and [[libfuzzer]].

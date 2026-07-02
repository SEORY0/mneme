---
type: causal-policy
title: "PDF Xref Stream Construct Parser Reached Xref Cleanup Crash Invalid Memory Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached_xref_cleanup_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_xref_cleanup_crash"
candidate_family: "construct"
input_format: "pdf-xref-stream"
harness_convention: "libfuzzer-mupdf-pdf-renderer"
vuln_class: "invalid-memory-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-xref-cleanup-crash", "pdf-xref-stream", "libfuzzer-mupdf-pdf-renderer", "construct", "invalid-memory-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached_xref_cleanup_crash", "pdf-xref-stream", "libfuzzer-mupdf-pdf-renderer", "invalid-memory-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# PDF Xref Stream Construct Parser Reached Xref Cleanup Crash Invalid Memory Read Verified Recovery

## Policy
For `generic_crash x parser_reached_xref_cleanup_crash`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal renderable PDF with a valid catalog and page tree, then use an xref stream whose index ranges first create a subsection and later overlap while extending it.
2. The overlap-and-extend case reaches the wrong subsection-entry initialization path while the surrounding document stays coherent enough for MuPDF to finish document teardown.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The input is a raw PDF byte stream with header, indirect objects, catalog/pages/page structure, stream objects, an xref stream dictionary, and trailer linkage.
- Xref streams use width metadata and index ranges to describe object-entry records; multiple ranges can describe separate or overlapping subsections.
- Harness [[libfuzzer-mupdf-pdf-renderer]]:
  - The MuPDF libFuzzer target opens the input bytes directly as an in-memory PDF and then exercises page counting/rendering under the fuzzer allocator.
  - There is no outer archive, no mode selector, and no FuzzedDataProvider layout; parser exceptions are caught unless a sanitizer-visible memory error occurs.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[pdf-xref-stream]] and [[libfuzzer-mupdf-pdf-renderer]].

---
type: causal-policy
title: DWG Legacy Section Bounds Recovery
description: Recover legacy DWG decoder crashes by selecting a pre-modern header and sparse section metadata.
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch_official_match
candidate_family: construct
input_format: dwg
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-write
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, official_match, dwg, legacy_decoder, section_bounds]
match_keys: [wrong_sink, parser_reached_sink_mismatch_official_match, dwg, legacy_section]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For DWG targets, choose the legacy decoder explicitly before testing malformed table and section bounds. Sparse but coherent section metadata can drive the decoder into section-header handling before first-object lookup completes.

## Procedure
1. Use a legacy DWG header that selects the older decode path.
2. Keep the initial control-table metadata recognizable but sparse.
3. Make section headers inconsistent enough to violate bounds during section handling.
4. Do not rely on random bytes after the header; they usually fail before the legacy path.
5. Submit parser-reached sink-mismatch crashes when official comparison is available.

## Negative Memory
- Do not use modern DWG headers for legacy section bugs.
- Do not overfill the object table while diagnosing section-header handling.
- Do not discard a local wrong-sink crash if official verification confirms the target.

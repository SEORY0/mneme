---
type: causal-policy
title: "No Crash Pdf Rendered Without Annotation Sentinel Crash Pdf Construct Pdf Page Annotation Variadic Sentinel Missing Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal pdf_rendered_without_annotation_sentinel_crash."
failure_class: "no_crash"
verifier_signal: "pdf_rendered_without_annotation_sentinel_crash"
candidate_family: "construct_pdf_page_annotation"
input_format: "pdf"
harness_convention: "libfuzzer-mupdf-pdf-renderer"
vuln_class: "variadic-sentinel-missing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pdf-rendered-without-annotation-sentinel-crash", "pdf", "negative-memory", "round-14"]
match_keys: ["no_crash", "pdf_rendered_without_annotation_sentinel_crash", "pdf", "libfuzzer-mupdf-pdf-renderer", "variadic-sentinel-missing", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Pdf Rendered Without Annotation Sentinel Crash Pdf Construct Pdf Page Annotation Variadic Sentinel Missing Negative Memory

- key: `no_crash x pdf_rendered_without_annotation_sentinel_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer-mupdf-pdf-renderer]]

## Failure Shape
Minimal renderable PDFs with page structure and an annotation did not trigger the missing variadic sentinel crash. The likely missing gate is a specific annotation rendering path or structure-tree lookup that reaches the unterminated dictionary-key lookup with stack contents that are not benign.

## Policy
Treat `no_crash x pdf_rendered_without_annotation_sentinel_crash` on `pdf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.

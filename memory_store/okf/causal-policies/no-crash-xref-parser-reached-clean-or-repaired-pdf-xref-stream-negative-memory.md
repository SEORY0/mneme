---
type: causal-policy
title: "No Crash Xref Parser Reached Clean Or Repaired Pdf Xref Stream Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal xref_parser_reached_clean_or_repaired."
failure_class: "no_crash"
verifier_signal: "xref_parser_reached_clean_or_repaired"
candidate_family: "construct"
input_format: "pdf xref stream"
harness_convention: "libfuzzer mupdf pdf renderer"
vuln_class: "xref-index-out-of-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "xref-parser-reached-clean-or-repaired", "pdf-xref-stream", "libfuzzer-mupdf-pdf-renderer", "negative-memory", "round-17"]
match_keys: ["no-crash", "xref-parser-reached-clean-or-repaired", "pdf-xref-stream", "libfuzzer-mupdf-pdf-renderer", "xref-index-out-of-bounds", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Xref Parser Reached Clean Or Repaired Pdf Xref Stream Negative Memory

- key: `no_crash x xref_parser_reached_clean_or_repaired`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-xref-stream]]
- related harness facts: [[libfuzzer-mupdf-pdf-renderer]]

## Failure Shape
- Minimal xref-stream PDFs reached MuPDF xref parsing, including corrupt width arrays and an index table larger than the declared table size, but the parser either repaired the document or rejected object lookup before the target xref-index access crashed.

## Policy
Treat `no_crash x xref_parser_reached_clean_or_repaired` on `pdf xref stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `xref_parser_reached_clean_or_repaired`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pdf-xref-stream]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-mupdf-pdf-renderer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

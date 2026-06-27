---
type: causal-policy
title: "No Crash PDF Header Accepted Render Path Not Reached PDF Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal pdf_header_accepted_render_path_not_reached."
failure_class: "no_crash"
verifier_signal: "pdf_header_accepted_render_path_not_reached"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-ghostscript"
vuln_class: "invalid-colorspace-validation"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "pdf-header-accepted-render-path-not-reached", "pdf", "libfuzzer-ghostscript", "negative-memory", "round-18"]
match_keys: ["no-crash", "pdf-header-accepted-render-path-not-reached", "pdf", "libfuzzer-ghostscript", "invalid-colorspace-validation", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash PDF Header Accepted Render Path Not Reached PDF Negative Memory

- key: `no_crash x pdf_header_accepted_render_path_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer-ghostscript]]

## Failure Shape
- Indexed color-space PDFs with invalid and valid bases, alternate index values, fill and stroke painting, and a graphics-state-wrapped fill all parsed without reaching the specific PostScript/PDF color-space validation sink.
- The likely missing gate is a resource arrangement that forces Ghostscript to instantiate the invalid Indexed base in the same path as the fixed check.

## Policy
Treat `no_crash x pdf_header_accepted_render_path_not_reached` on `pdf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `pdf_header_accepted_render_path_not_reached`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pdf]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ghostscript]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x pdf_header_accepted_render_path_not_reached`.
- Candidate family: `construct`.
- Basin summary: Indexed color-space PDFs with invalid and valid bases, alternate index values, fill and stroke painting, and a graphics-state-wrapped fill all parsed without reaching the specific PostScript/PDF color-space validation sink.

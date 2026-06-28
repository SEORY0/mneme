---
type: causal-policy
title: "No Crash PDF Header Parser Reached No Sanitizer Signal PDF Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal pdf_header_parser_reached_no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "pdf_header_parser_reached_no_sanitizer_signal"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-stack-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "pdf-header-parser-reached-no-sanitizer-signal", "pdf", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "pdf-header-parser-reached-no-sanitizer-signal", "pdf", "libfuzzer", "uninitialized-stack-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash PDF Header Parser Reached No Sanitizer Signal PDF Negative Memory

- key: `no_crash x pdf_header_parser_reached_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Short PDF-version headers reached MuPDF's version parsing path and produced parser warnings, but did not produce a sanitizer-detected read from uninitialized stack bytes.
- Adding minimal repair-oriented PDF structure changed parser depth but did not expose the described version-buffer initialization bug locally.

## Policy
Treat `no_crash x pdf_header_parser_reached_no_sanitizer_signal` on `pdf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `pdf_header_parser_reached_no_sanitizer_signal`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pdf]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x pdf_header_parser_reached_no_sanitizer_signal`.
- Candidate family: `construct`.
- Basin summary: Short PDF-version headers reached MuPDF's version parsing path and produced parser warnings, but did not produce a sanitizer-detected read from uninitialized stack bytes.

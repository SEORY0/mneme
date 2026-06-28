---
type: negative-memory
title: "No Crash Dxf Parser Clean Exit Dxf Text Construct Double Free Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal dxf_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "dxf_parser_clean_exit"
candidate_family: "construct"
input_format: "dxf-text"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dxf-parser-clean-exit", "dxf-text", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "dxf_parser_clean_exit", "dxf-text", "libfuzzer", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Dxf Parser Clean Exit Dxf Text Construct Double Free Negative Memory

- key: `no_crash x dxf_parser_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dxf-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A minimal DXF text document with header, tables, and objects scaffolding executed cleanly. It did not reproduce the INVALIDDWG import-error path where the imported filename allocation is freed twice.

## Policy
Treat `no_crash x dxf_parser_clean_exit` on `dxf-text` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `dxf_parser_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `dxf_parser_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
DXF is a line-oriented group-code/value format with SECTION and ENDSEC delimiters. OBJECTS sections can contain dictionaries and index-like objects referenced by handle-valued group pairs.

## Harness Contract
The LibreDWG fuzzer detects DWG by an AC prefix, JSON by an object prefix, and otherwise treats raw NUL-terminated input as DXF text. After reading, it writes the decoded drawing to one of several output formats.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 1 attempt.
- Scope: generator repair and basin avoidance only.

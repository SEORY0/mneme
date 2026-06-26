---
type: causal-policy
title: "PDF Construct PDF Repair Parser Reached Out Of Bounds Read Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal pdf_repair_parser_reached."
failure_class: "generic_crash"
verifier_signal: "pdf_repair_parser_reached"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "pdf-repair-parser-reached", "pdf", "construct", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "pdf_repair_parser_reached", "pdf", "libfuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# PDF Construct PDF Repair Parser Reached Out Of Bounds Read Verified Recovery

## Policy
For `generic_crash x pdf_repair_parser_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Feed a minimal damaged PDF that forces Ghostscript into xref repair rather than normal xref loading. Include an object stream dictionary with inconsistent object-stream metadata so repair discovers and frees malformed PDF objects while rebuilding cross-reference state.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A PDF can enter repair mode when its xref information is absent or invalid. Object streams are indirect stream objects whose dictionary declares object count, first-object area, and stream length; malformed metadata can be encountered during repair scanning.
- Harness: The Ghostscript raster fuzzer sends raw input as the interpreter input stream using the cups raster device path. There is no byte carving; parser reachability depends on the document syntax forcing the PDF interpreter and repair code.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

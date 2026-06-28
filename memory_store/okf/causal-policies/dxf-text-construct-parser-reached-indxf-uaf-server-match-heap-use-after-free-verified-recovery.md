---
type: causal-policy
title: "DXF Text Construct Parser Reached Indxf Uaf Server Match Heap Use After Free Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal parser_reached_indxf_uaf_server_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_indxf_uaf_server_match"
candidate_family: "construct"
input_format: "DXF text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-indxf-uaf-server-match", "dxf-text", "construct", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "parser_reached_indxf_uaf_server_match", "DXF text", "libfuzzer", "heap-use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# DXF Text Construct Parser Reached Indxf Uaf Server Match Heap Use After Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_indxf_uaf_server_match`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal DXF document with valid header/table scaffolding, then put an objects section
  containing a dictionary entry that names an index object and the index object itself.
1. This reaches the DXF object reader path where the current pair is freed but later inspected as
  the object parsing loop advances.

## Format Contract
- DXF is a line-oriented group-code/value format.
- A minimal document can declare SECTION/ENDSEC groups, set the version in the HEADER section,
  provide basic TABLES scaffolding, and define OBJECTS entries such as dictionaries and index
  objects.
- Object references are represented by handle-valued group pairs.

## Harness Contract
- The LibreDWG libFuzzer harness chooses the parser from the raw input prefix: DWG data begins with
  an AC signature, JSON begins with an opening object brace, and other inputs are treated as DXF
  text after null-termination is enforced.
- After reading, the harness writes the decoded drawing through a randomly selected output format.

## Related Knowledge
- Format facts: [[dxf-text]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

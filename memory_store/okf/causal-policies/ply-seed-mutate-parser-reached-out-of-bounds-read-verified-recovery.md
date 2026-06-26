---
type: causal-policy
title: "PLY Seed Mutate Parser Reached Out Of Bounds Read Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "ply"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "ply", "seed-mutate", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "parser_reached", "ply", "libfuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# PLY Seed Mutate Parser Reached Out Of Bounds Read Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a compact PLY-like buffer that preserves the initial magic and enough of a binary format declaration for Assimp's signature-based PLY importer to select the parser, then make the following header line malformed and effectively unterminated with non-line-ending filler. The vulnerable IOStreamBuffer line reader advances from an earlier line state into the header parse and reads past the valid cache while searching for a line terminator; the fixed build consumes CR/LF state more defensively and exits cleanly.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- PLY inputs begin with a magic line, a format declaration, header records such as comments or element/property declarations, an end-header marker, and then either ASCII rows or binary element data. Assimp selection is content-based in this harness, so the earliest bytes must be recognizable as PLY even when later header syntax is malformed. Binary PLY parsing reads header lines through IOStreamBuffer before switching to block reads for element data.
- Harness: The libFuzzer harness passes the entire input buffer to Assimp Importer::ReadFileFromMemory with no extension and no outer selector. Importer detection is signature-based, and successful reachability is visible from the PLY importer log before parser crashes.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

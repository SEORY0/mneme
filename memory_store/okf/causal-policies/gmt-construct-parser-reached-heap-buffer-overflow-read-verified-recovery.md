---
type: causal-policy
title: "GMT Construct Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "gmt"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "gmt", "construct", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "parser_reached", "gmt", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# GMT Construct Parser Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Provide a tiny GMT ASCII vector datasource header that satisfies the OGR_GMT driver identification marker, then include a truncated keyed projection metadata token. The header parser stores keyed values from comment metadata, and the vulnerable constructor assumes a projection key has both a projection-kind discriminator and an argument. A key that ends immediately after the projection marker makes it build a string from past the allocated key buffer, producing a heap over-read before feature data is needed.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- OGR GMT vector files are line-oriented text. Driver selection depends on an early GMT version marker in a comment/header line. Header metadata uses at-sign keyed tokens; geometry type, region, field names/types, and projection metadata are parsed before feature rows. A full feature section is not required to reach header metadata parsing.
- Harness: The libFuzzer target writes the raw input to a temporary file and opens it through GDAL/OGR vector autodetection. There is no selector byte or structured harness prefix; the bytes must simply form enough of a file-backed datasource for the OGR_GMT driver identify/open path.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

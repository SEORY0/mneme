---
type: causal-policy
title: Parser Reached Clean Negative Memory
description: Negative memory for clean exits after the relevant parser or harness surface was reached.
failure_class: no_crash
verifier_signal: parser_reached_clean
candidate_family: seed_mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, parser_reached_clean, negative_memory, boundary_not_violated]
match_keys: [no_crash, parser_reached_clean, negative_memory, boundary_not_violated]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A parser-reached clean exit means the current format carrier is valid but the invariant remains satisfied. Keep the carrier and move to the smallest field that can violate the named boundary under the reached parser mode.

## Procedure
1. Preserve the seed or constructed envelope that reached the parser.
2. Identify the invariant still satisfied: table length, glyph selection, alpha state, TCP slice bounds, palette selection, or record escape state.
3. Mutate only the field that breaks that invariant while preserving the mode selector.
4. Prefer truncation or inconsistent metadata over appending unrelated data.
5. Stop when further mutations leave the parser mode or become bad-format evidence.

## Negative Memory
- Do not restart from random bytes after parser reachability is proven.
- Do not change multiple metadata families at once; clean exits need causal isolation.
- Do not submit parser-clean candidates.

## Evidence Shape
- Support: multiple diagnosed round failures with parser-reached clean signals.
- Scope: generator repair only.

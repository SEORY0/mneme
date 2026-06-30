---
type: causal-policy
title: "Opentype Font Seed Mutate Parser Reached Stack Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "opentype-font", "libfuzzer", "seed-mutate", "stack-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached", "opentype-font", "libfuzzer", "stack-buffer-overflow-read", "verified_recovery", "seed-mutate", "stack-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Opentype Font Seed Mutate Parser Reached Stack Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid SFNT/OpenType font that contains a version-2 glyph-name table. Preserve the font and append the harness trailer so the shape fuzzer asks the face test to round-trip an existing glyph name. This reaches glyph-name lookup, where the vulnerable build passes an overloaded address for an hb_bytes_t search key into the binary search comparator.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[opentype-font]]: The input is an SFNT/OpenType font with a table directory and a post table capable of mapping glyph IDs to names. The parser accepts extra trailing bytes after the font data, which can be used by the harness as text/control material without invalidating the font.
- Harness [[libfuzzer]]: The libFuzzer target consumes raw bytes as a font blob. Its shape path copies a fixed-size trailer from the end of the input into a UTF-32 text buffer and then runs face API checks using that trailer-selected codepoint; there is no FuzzedDataProvider layout.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[opentype-font]] and [[libfuzzer]].

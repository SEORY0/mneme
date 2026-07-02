---
type: causal-policy
title: "Opentype Font Seed Mutate No Crash Font Parser Reached Clean Exit Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for opentype-font candidates that ended in no_crash with verifier signal font_parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "font_parser_reached_clean_exit"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-shape-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-parser-reached-clean-exit", "opentype-font", "libfuzzer-harfbuzz-shape-fuzzer", "seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-32"]
match_keys: ["no-crash", "font-parser-reached-clean-exit", "opentype-font", "libfuzzer-harfbuzz-shape-fuzzer", "seed-mutate", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Opentype Font Seed Mutate No Crash Font Parser Reached Clean Exit Heap Buffer Overflow Read Negative Memory

- key: `no_crash x font_parser_reached_clean_exit`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-harfbuzz-shape-fuzzer]]

## Policy
Treat `no_crash x font_parser_reached_clean_exit` for `[[opentype-font]]` under `[[libfuzzer-harfbuzz-shape-fuzzer]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Valid sfnt carriers exercised the shape harness but did not reach a sanitizer-visible offset dereference. Legacy kern format-2 mutations, EOF table placement, high-glyph cmap steering, a color-SVG invalid index probe, and an AAT kerx format-2 probe all exited cleanly. The likely missing gate is a dispatch path that actually applies the malformed AAT offset table rather than merely sanitizing or ignoring it.
3. Rebuild around `[[opentype-font]]` and `[[libfuzzer-harfbuzz-shape-fuzzer]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- The input is a complete sfnt/OpenType font with a table directory mapping tags to table bodies. Layout and AAT subtables use relative offsets from table or subtable bases; class-table based kerning formats combine class lookups with a kerning array. AAT kerx has a table header followed by one or more subtables with coverage, format, and format-specific relative offsets.

## Harness Contract
- The HarfBuzz shape fuzzer consumes raw font bytes as one hb_blob, creates an hb_face and hb_font, shapes fixed ASCII text, then shapes a UTF-32 buffer copied from the input trailer. It also calls miscellaneous face/font APIs for color, math, name, variation, glyph origin, and glyph extents. No external wrapper, checksum, mode selector, or FuzzedDataProvider layout is present.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 5.

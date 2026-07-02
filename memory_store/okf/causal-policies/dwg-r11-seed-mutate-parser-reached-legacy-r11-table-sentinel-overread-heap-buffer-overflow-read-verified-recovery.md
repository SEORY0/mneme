---
type: causal-policy
title: "Dwg R11 Seed Mutate Parser Reached Legacy R11 Table Sentinel Overread Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached_legacy_r11_table_sentinel_overread."
failure_class: "generic_crash"
verifier_signal: "parser_reached_legacy_r11_table_sentinel_overread"
candidate_family: "seed_mutate"
input_format: "dwg-r11"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-legacy-r11-table-sentinel-overread", "dwg-r11", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached_legacy_r11_table_sentinel_overread", "dwg-r11", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Dwg R11 Seed Mutate Parser Reached Legacy R11 Table Sentinel Overread Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_legacy_r11_table_sentinel_overread`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a real legacy R11 DWG seed so the version, header variables, entity ranges, CRC material, and sentinels remain coherent.
2. Preserve a legacy table record's plausible size and count, but make its declared payload address fall before the required sentinel prefix.
3. The R11 table decoder subtracts the sentinel prefix from that address, wraps the cursor, and then the unknown/sentinel read copies from outside the input buffer.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- R11 DWG files start with an AutoCAD release marker and carry a legacy header with entity, block, and extra-entity ranges plus table records containing size, count, flags, and payload address fields.
- R11 sections are guarded by fixed sentinels, and the table payload address is expected to point after the section's begin sentinel.
- Small entity-size, block-range, EED, or clean seed mutations can preserve parser reachability but miss this table-address relation.
- Harness [[libfuzzer]]:
  - The LibreDWG libFuzzer target consumes raw file bytes.
  - Inputs with the DWG release prefix go to the binary DWG decoder, JSON-looking inputs go to JSON import, and other inputs fall back to DXF text import.
  - No fuzzer-side carving or FuzzedDataProvider layout is used; this crash occurs during DWG decode before output-format selection matters.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[dwg-r11]] and [[libfuzzer]].

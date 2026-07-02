---
type: causal-policy
title: "Opentype Truetype Sfnt Cpal Seed Mutate Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "seed_mutate"
input_format: "opentype-truetype-sfnt-cpal"
harness_convention: "libfuzzer-freetype-ftfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "opentype-truetype-sfnt-cpal", "libfuzzer-freetype-ftfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "parser_reached_target_sink", "opentype-truetype-sfnt-cpal", "libfuzzer-freetype-ftfuzzer", "heap-buffer-overflow-read", "generic-crash", "parser-reached-target-sink", "opentype-truetype-sfnt-cpal", "libfuzzer-freetype-ftfuzzer", "heap-buffer-overflow-read", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Opentype Truetype Sfnt Cpal Seed Mutate Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[opentype-truetype-sfnt-cpal]]
- related harness facts: [[libfuzzer-freetype-ftfuzzer]]

## Policy
For `generic_crash x parser_reached_target_sink` on `opentype-truetype-sfnt-cpal`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid small TrueType/SFNT seed so FreeType accepts the core face tables. Rebuild the SFNT directory with a CPAL table placed physically at the end of the input. Use CPAL version 1 with a short but otherwise coherent v0 header; declare enough palettes that the parser advances past the available palette-index area before reading the version-1 offset triplet. This reaches face initialization, enters CPAL loading, and makes the vulnerable parser read the version-1 offsets past the end of the fuzzer-owned font buffer. Broader variants that omitted the offset area entirely or corrupted palette color indices crashed the fixed build too.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[opentype-truetype-sfnt-cpal]]: A TrueType/OpenType SFNT file begins with a scaler tag and table directory, followed by tagged table payloads aligned for the table records. FreeType face setup needs coherent core tables such as head, hhea, hmtx, maxp, cmap, name, loca, glyf, and optional color tables. CPAL starts with version, palette-entry count, palette count, total color-record count, and first-color-record offset; version 1 then locates three additional offset fields after the per-palette color-index array.
- Harness [[libfuzzer-freetype-ftfuzzer]]: The FreeType ftfuzzer consumes raw font bytes unless the input is an uncompressed tar archive, in which case archive members become attached font files. There is no leading selector byte. The harness first opens the font to count faces, then opens selected faces and instances; SFNT face initialization loads optional CPAL/COLR data before the glyph-loading loop.

## Negative Memory
- Do not corrupt the outer `opentype-truetype-sfnt-cpal` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[opentype-truetype-sfnt-cpal]] and [[libfuzzer-freetype-ftfuzzer]].

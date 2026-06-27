---
type: causal-policy
title: "MD3 Seed Mutate Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 13 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "md3"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "md3", "seed-mutate", "verified-recovery", "round-13"]
match_keys: ["generic_crash", "parser_reached", "md3", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# MD3 Seed Mutate Parser Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid MD3 model so Assimp's signature detection, header validation, surface validation, mesh construction, and post-processing all succeed. Mutate only the main header's tag metadata so the model advertises a nonempty tag table, but the tag-table start leaves less than one full tag record in the file. The vulnerable loader validates surfaces but not the complete tag table before creating tag nodes, so it reads a tag name from beyond the available input.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- MD3 is a little-endian Quake mesh format with a fixed main header, model name, frame count, tag count, surface count, and offsets to frames, tags, surfaces, and EOF. Surface records contain their own counts and relative offsets for triangles, shaders, texture coordinates, vertices/normals, and the next surface. A valid seed can keep the surface data untouched while changing only the top-level tag table metadata. Tag records contain a fixed-size name followed by transform data and are consumed after mesh construction when the scene node tree is built.

## Harness Contract
- The oss-fuzz Assimp harness passes the raw libFuzzer byte buffer directly to Importer::ReadFileFromMemory with no extension hint. Format selection is signature based, and a recognized MD3 magic is enough to choose the MD3 importer. There is no leading mode byte, filename carving, or FuzzedDataProvider layout.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

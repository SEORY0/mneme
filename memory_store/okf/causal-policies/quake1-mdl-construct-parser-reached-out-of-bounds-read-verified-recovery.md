---
type: causal-policy
title: "Quake1 Mdl Construct Parser Reached Out Of Bounds Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "quake1-mdl"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "quake1-mdl", "libfuzzer", "construct", "out-of-bounds-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached", "quake1-mdl", "libfuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Quake1 Mdl Construct Parser Reached Out Of Bounds Read Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a raw Quake1 MDL model that satisfies the importer gates: recognized Quake MDL signature, accepted version, nonzero mesh counts, texture-coordinate and triangle sections, and a frame section.
2. Keep the mesh counts positive and use a grouped-frame record whose subframe count is negative, so the vulnerable loader computes the first simple-frame pointer before the model buffer while its size check only rejects pointers beyond the end.
3. A later vertex read through a normal triangle then dereferences that miscomputed frame-vertex pointer.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Quake1 MDL is a whole-file binary model.
- The header carries signature, version, scale/translation, skin dimensions, skin count, vertex count, triangle count, and frame count.
- After the header come optional skins, one texture-coordinate record per declared vertex, one triangle record per declared triangle, then frame data.
- Harness [[libfuzzer]]:
  - The Assimp libFuzzer harness passes the entire input byte array directly to Importer::ReadFileFromMemory with no selector byte and no FuzzedDataProvider carving.
  - Importer detection is signature based, and successful imports continue into the normal Assimp post-processing pipeline.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[quake1-mdl]] and [[libfuzzer]].

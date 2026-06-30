---
type: causal-policy
title: "Opentype Cff Seed Mutate Target Match Out Of Bounds Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal target_match."
failure_class: "generic_crash"
verifier_signal: "target_match"
candidate_family: "seed_mutate"
input_format: "opentype-cff"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match", "opentype-cff", "libfuzzer", "seed-mutate", "out-of-bounds-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "target_match", "opentype-cff", "libfuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Opentype Cff Seed Mutate Target Match Out Of Bounds Read Verified Recovery

## Policy
For `generic_crash x target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid CFF1 seac regression font.
2. Change the CFF charset from an explicit glyph-to-SID list into a compact range form that still covers the declared glyph count but omits the seac base or accent SID.
3. Keep the sfnt directory and checksums coherent, arrange the CFF table as the final declared table, and place the harness glyph selector outside declared table data.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- OpenType/CFF inputs are normal sfnt fonts with a table directory, padded table data, and a CFF Top DICT pointing to charset and CharStrings data.
- CFF charset format 0 lists one SID per glyph after .notdef, while charset formats 1 and 2 encode SID ranges whose covered glyph count is derived from range lengths.
- seac charstrings resolve base and accent standard-encoding codes through charset SID lookup before computing extents.
- Harness [[libfuzzer]]:
  - The libFuzzer harness feeds the whole byte stream as an hb_face font blob.
  - It also copies up to the final 64 input bytes into a fixed UTF-32 array; the last word of that array is passed as the glyph id to miscellaneous face/font APIs including glyph extents.
  - There is no leading mode selector or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[opentype-cff]] and [[libfuzzer]].

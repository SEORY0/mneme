---
type: causal-policy
title: "PDF With Opentype CFF Font Construct Target Match Confirmed Integer Overflow To Out Of Bounds Read Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal target_match_confirmed."
failure_class: "generic_crash"
verifier_signal: "target_match_confirmed"
candidate_family: "construct"
input_format: "pdf-with-opentype-cff-font"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-to-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match-confirmed", "pdf-with-opentype-cff-font", "construct", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "target_match_confirmed", "pdf-with-opentype-cff-font", "libfuzzer", "integer-overflow-to-out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# PDF With Opentype CFF Font Construct Target Match Confirmed Integer Overflow To Out Of Bounds Read Verified Recovery

## Policy
For `generic_crash x target_match_confirmed`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Embed a Type1C font stream in a minimal PDF and make the OpenType table directory describe a CFF table whose offset plus length wraps in the vulnerable 32-bit check while the stream length remains small and apparently valid. Rendering text forces Ghostscript to load that table and read from the wrapped pointer; the fixed build rejects the table bounds.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A Type1C PDF font stream can contain an OpenType wrapper around CFF data. The table directory carries a table offset and table length, and those fields must be validated without wraparound before narrowing the font buffer to the CFF subtable.
- Harness: The gs_device_psdcmyk libFuzzer target consumes raw PDF bytes and renders a page through Ghostscript. Selecting an embedded font in page content is sufficient to reach PDF font loading and CFF table extraction.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

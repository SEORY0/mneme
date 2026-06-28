---
type: causal-policy
title: "PDF With Opentype CFF Font Seed Mutate Target Match Confirmed Stack Buffer Overflow Write Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal target_match_confirmed."
failure_class: "generic_crash"
verifier_signal: "target_match_confirmed"
candidate_family: "seed_mutate"
input_format: "pdf-with-opentype-cff-font"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match-confirmed", "pdf-with-opentype-cff-font", "seed-mutate", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "target_match_confirmed", "pdf-with-opentype-cff-font", "libfuzzer", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# PDF With Opentype CFF Font Seed Mutate Target Match Confirmed Stack Buffer Overflow Write Verified Recovery

## Policy
For `generic_crash x target_match_confirmed`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Embed a real OpenType CFF font in a minimal PDF and mutate its CFF private dictionary so multiple blue/stem delta arrays contain more operands than Ghostscript fixed Type1 private arrays can hold. Rendering text with that font forces the CFF dictionary reader to copy the oversized operand stack into fixed structures; the fixed build rejects or bounds the condition.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A PDF Type1 font can reference a FontDescriptor with a Type1C FontFile stream. OpenType CFF fonts carry a table directory and a CFF private dictionary; blue value and stem snap fields are delta arrays consumed while constructing Ghostscript Type1 private data.
- Harness: The gstoraster libFuzzer target consumes raw PDF/PostScript-like bytes and invokes Ghostscript rendering. A minimal page that selects the embedded font is enough to force font loading during page interpretation; there is no mode byte or FuzzedDataProvider contract.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

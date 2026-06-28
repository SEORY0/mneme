---
type: causal-policy
title: "Blosc Chunk Construct Official Target Match Out Of Bounds Read Verified Recovery"
description: "Round 9 verified recovery for generic_crash with verifier signal official_target_match."
failure_class: "generic_crash"
verifier_signal: "official_target_match"
candidate_family: "construct"
input_format: "blosc chunk"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match", "blosc-chunk", "construct", "verified-recovery", "round-9"]
match_keys: ["generic_crash", "official_target_match", "blosc chunk", "libfuzzer", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Blosc Chunk Construct Official Target Match Out Of Bounds Read Verified Recovery

## Policy
For `generic_crash x official_target_match`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a self-consistent raw Blosc chunk whose header-reported compressed size equals the total
  input and whose decompressed size is nonzero.
1. Use a split multi-stream block so the parser iterates stream records.
1. Make an early stream use a negative compressed-size marker with an extreme magnitude; keep
  following stream metadata present so validation reaches decompression.
1. The vulnerable image reads past the logical stream boundary, while the fixed image rejects or
  handles the malformed negative-size stream.

## Format Contract
- A Blosc chunk starts with a compact header containing version, flags, type size, uncompressed
  size, block size, and compressed size, followed by block-start entries and per-stream records.
- Split blocks use one stream per type lane; negative stream sizes encode special runs and are the
  important malformed field family here.

## Harness Contract
- The libFuzzer target receives raw chunk bytes.
- It rejects inputs shorter than the minimum header, requires the header compressed size to equal
  the file size and the uncompressed size to be nonzero, validates the compressed buffer, then calls
  chunk decompression into an allocated output buffer.

## Related Knowledge
- Format facts: [[blosc-chunk]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.

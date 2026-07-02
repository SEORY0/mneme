---
type: causal-policy
title: "Jpeg Exif Seed Mutate Generic Crash Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for jpeg-exif when generic_crash pairs with parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "seed_mutate"
input_format: "jpeg-exif"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "jpeg-exif", "libfuzzer", "seed-mutate", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "parser-reached-target-sink", "jpeg-exif", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Jpeg Exif Seed Mutate Generic Crash Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[jpeg-exif]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- candidate family: `seed_mutate`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[jpeg-exif]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x parser_reached_target_sink` appears for `jpeg-exif`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[jpeg-exif]] format contract before changing sink fields.
2. Recreate the verified causal relation: Start from a valid JPEG seed and insert a syntactically valid EXIF profile. Keep the TIFF header and first IFD coherent enough for the JPEG reader to request the orientation attribute, then give the orientation directory entry a string-like format with an intentionally oversized component count. This preserves parser reachability while making the vulnerable EXIF attribute generator copy past the mapped profile buffer; the fixed build rejects or bounds the relation.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
JPEG accepts metadata in APP segments, and EXIF metadata contains a TIFF-style byte-order header, a first-IFD pointer, and directory entries carrying tag, format, component count, and either inline value bytes or an offset into the profile. Orientation is queried automatically by the JPEG reader after image decode, so the EXIF envelope must be attached to a valid JPEG carrier.

### Harness Contract
The libFuzzer target feeds the raw input bytes directly to the GraphicsMagick JPEG coder through a memory blob. There is no selector byte, no FuzzedDataProvider split, and no filename extension gate beyond the compiled JPEG coder.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `seed_mutate`.
- Verifier key: `generic_crash x parser_reached_target_sink`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.

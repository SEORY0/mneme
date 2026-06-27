---
type: causal-policy
title: "C Blosc2 Frame Seed Mutate Parser Reached Frame Get Vlmetalayers Invalid Negative Length Memory Access Verified Recovery"
description: "Round 13 verified recovery for generic_crash with verifier signal parser_reached_frame_get_vlmetalayers."
failure_class: "generic_crash"
verifier_signal: "parser_reached_frame_get_vlmetalayers"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "libfuzzer whole-buffer frame decompressor"
vuln_class: "invalid-negative-length-memory-access"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-frame-get-vlmetalayers", "c-blosc2-frame", "seed-mutate", "verified-recovery", "round-13"]
match_keys: ["generic_crash", "parser_reached_frame_get_vlmetalayers", "c-blosc2-frame", "libfuzzer whole-buffer frame decompressor", "invalid-negative-length-memory-access", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# C Blosc2 Frame Seed Mutate Parser Reached Frame Get Vlmetalayers Invalid Negative Length Memory Access Verified Recovery

## Policy
For `generic_crash x parser_reached_frame_get_vlmetalayers`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid contiguous c-blosc2 frame seed so the frame header, frame length, chunk table, trailer length footer, and decompressor setup remain valid. Replace only the variable-length metalayer trailer body with a reader-compatible indexed entry whose content marker is present but whose signed content length is negative. The vulnerable trailer parser stores that negative length and then uses it as an allocation/copy size; the fixed build rejects the negative length.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A c-blosc2 frame begins with a msgpack-like frame header containing the frame magic/name, declared frame length, byte counts, chunk size/count, optional metadata flags, chunk offsets, compressed chunks, and a trailer. The trailer includes a versioned array, a variable-length metalayer section, a declared trailer length near the footer, and a fingerprint extension footer. Variable-length metalayers are represented by a small name-to-content-offset index and serialized bin content records.

## Harness Contract
- The fuzzer feeds the whole PoC buffer directly to blosc2_schunk_from_buffer. If the frame opens, it allocates a destination from the declared uncompressed byte count and attempts chunk decompression. There is no selector byte, filename wrapper, checksum recomputation requirement, or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
## Round 13 Reinforcement

- key: `generic_crash x parser_reached_frame_get_vlmetalayers`
- candidate family: `seed_mutate`
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[libfuzzer-whole-buffer-frame-decompressor]]

### Procedure Delta
Start from a valid contiguous c-blosc2 frame seed so the frame header, frame length, chunk table, trailer length footer, and decompressor setup remain valid. Replace only the variable-length metalayer trailer body with a reader-compatible indexed entry whose content marker is present but whose signed content length is negative. The vulnerable trailer parser stores that negative length and then uses it as an allocation/copy size; the fixed build rejects the negative length.

### Format Contract Delta
A c-blosc2 frame begins with a msgpack-like frame header containing the frame magic/name, declared frame length, byte counts, chunk size/count, optional metadata flags, chunk offsets, compressed chunks, and a trailer. The trailer includes a versioned array, a variable-length metalayer section, a declared trailer length near the footer, and a fingerprint extension footer. Variable-length metalayers are represented by a small name-to-content-offset index and serialized bin content records.

### Harness Contract Delta
The fuzzer feeds the whole PoC buffer directly to blosc2_schunk_from_buffer. If the frame opens, it allocates a destination from the declared uncompressed byte count and attempts chunk decompression. There is no selector byte, filename wrapper, checksum recomputation requirement, or FuzzedDataProvider carving.

### Evidence Shape
- Support: additional round-13 official target match.
- Scope: generator repair for the same failure-keyed basin.

---
type: causal-policy
title: "Dng Construct Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "dng"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "dng", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_but_official_target_match", "dng", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Dng Construct Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a real DNG/TIFF carrier rather than the standalone opcode-fuzzer envelope: make an uncompressed one-strip DNG with an opcode-list tag so the decoder reads image data and then applies stage-one opcodes.
2. Inside the big-endian opcode list, use a row or column delta/scale opcode whose vector length satisfies the pitch-derived expected-count rule, but choose a non-unit pitch so the apply loop later passes the raw image coordinate to the opcode callback.
3. The vulnerable build indexes the compact delta vector by that raw coordinate; the fixed build normalizes by the pitch before indexing.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- DNG is a TIFF container: byte order and IFD entries must be coherent; a DNG version tag selects the DNG decoder; baseline image tags for dimensions, sample layout, compression, photometric interpretation, strip location, strip byte count, and sample format allow an uncompressed strip to decode.
- DNG opcode lists are stored as big-endian data blobs even when the surrounding TIFF is little-endian.
- An opcode list contains an opcode count followed by code, version, flags, payload length, and opcode-specific payload.
- Harness [[libfuzzer]]:
  - The selected target consumes raw TIFF/DNG file bytes through RawSpeed's TIFF decoder fuzzer; there is no prefix byte or FuzzedDataProvider layout.
  - The standalone DNG-opcode fuzzer has a little-endian RawImage prefix followed by a big-endian opcode stream, but that envelope does not reach this packaged target.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[dng]] and [[libfuzzer]].

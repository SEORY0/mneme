---
type: causal-policy
title: "No Crash Frame Parser Clean Without Usermeta Crash C Blosc2 Frame Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal frame_parser_clean_without_usermeta_crash."
failure_class: "no_crash"
verifier_signal: "frame_parser_clean_without_usermeta_crash"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "libfuzzer-decompress-frame"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "frame-parser-clean-without-usermeta-crash", "c-blosc2-frame", "negative-memory", "round-13"]
match_keys: ["no_crash", "frame_parser_clean_without_usermeta_crash", "c-blosc2-frame", "libfuzzer-decompress-frame", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Frame Parser Clean Without Usermeta Crash C Blosc2 Frame Negative Memory

- key: `no_crash x frame_parser_clean_without_usermeta_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[libfuzzer-decompress-frame]]

## Failure Shape
Valid in-repo Blosc2 frame seeds reached the decompress-frame target, but mutating only the trailer usermeta length across boundary and large regimes, and mutating only the trailer length field across short and overlong regimes, exited cleanly. Official submit for the largest bounded usermeta-length mutation also exited clean, so the missing trigger is likely another accepted frame-size/trailer-offset relation rather than the usermeta length field alone.

## Policy
Treat `no_crash x frame_parser_clean_without_usermeta_crash` on `c-blosc2-frame` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `frame_parser_clean_without_usermeta_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
A C-Blosc2 frame has a msgpack-like header with frame magic, header size, declared frame size, flags, codec metadata, sizes, chunk metadata, chunk payloads, and a trailer. The trailer stores a usermeta chunk as a binary object with its own length and a separate trailer length near the end. The target read derives the trailer offset from frame length and trailer length, then reads usermeta metadata from that trailer.

## Harness Contract
The libFuzzer decompress-frame target passes the whole raw input to blosc2_schunk_open_sframe. If frame reconstruction succeeds, it allocates an output buffer from the parsed uncompressed size, attempts chunk decompression, then frees the reconstructed super-chunk. There is no leading selector byte or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x frame_parser_clean_without_usermeta_crash`
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[libfuzzer-decompress-frame]]

### Failure Shape Delta
Valid in-repo Blosc2 frame seeds reached the decompress-frame target, but mutating only the trailer usermeta length across boundary and large regimes, and mutating only the trailer length field across short and overlong regimes, exited cleanly. Official submit for the largest bounded usermeta-length mutation also exited clean, so the missing trigger is likely another accepted frame-size/trailer-offset relation rather than the usermeta length field alone.

### Format Contract Delta
A C-Blosc2 frame has a msgpack-like header with frame magic, header size, declared frame size, flags, codec metadata, sizes, chunk metadata, chunk payloads, and a trailer. The trailer stores a usermeta chunk as a binary object with its own length and a separate trailer length near the end. The target read derives the trailer offset from frame length and trailer length, then reads usermeta metadata from that trailer.

### Harness Contract Delta
The libFuzzer decompress-frame target passes the whole raw input to blosc2_schunk_open_sframe. If frame reconstruction succeeds, it allocates an output buffer from the parsed uncompressed size, attempts chunk decompression, then frees the reconstructed super-chunk. There is no leading selector byte or FuzzedDataProvider carving.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

---
type: causal-policy
title: "Png Raw Profile Text Chunk Construct Parser Reached Sink Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal parser_reached_sink_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "png-raw-profile-text-chunk"
harness_convention: "libfuzzer-graphicsmagick-coder-png"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-sink-match", "png-raw-profile-text-chunk", "libfuzzer-graphicsmagick-coder-png", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "parser_reached_sink_match", "png-raw-profile-text-chunk", "libfuzzer-graphicsmagick-coder-png", "heap-buffer-overflow-read", "generic-crash", "parser-reached-sink-match", "png-raw-profile-text-chunk", "libfuzzer-graphicsmagick-coder-png", "heap-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Png Raw Profile Text Chunk Construct Parser Reached Sink Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_sink_match`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[png-raw-profile-text-chunk]]
- related harness facts: [[libfuzzer-graphicsmagick-coder-png]]

## Policy
For `generic_crash x parser_reached_sink_match` on `png-raw-profile-text-chunk`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a syntactically valid minimal PNG so libpng reaches text-chunk processing. Add a text metadata entry whose key selects GraphicsMagick raw-profile handling, then violate the raw-profile text grammar by omitting the expected separator before the declared profile fields. The vulnerable reader scans past the heap buffer while looking for that separator; the fixed build rejects the malformed raw profile cleanly.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[png-raw-profile-text-chunk]]: PNG files require the standard PNG signature, an image header chunk, valid chunk lengths and CRCs, image data, and an end chunk. Text metadata chunks store a keyword, a separator byte, and a text payload. GraphicsMagick treats keywords with the raw-profile prefix as hex-encoded profile records whose text payload normally contains a profile label line, a length field, and hex profile data.
- Harness [[libfuzzer-graphicsmagick-coder-png]]: The GraphicsMagick coder fuzzer passes the raw libFuzzer bytes directly as an in-memory image blob to a fixed PNG coder instance. There is no harness byte carving. The image must be a valid enough PNG for libpng to expose text metadata to GraphicsMagick after basic chunk validation.

## Negative Memory
- Do not corrupt the outer `png-raw-profile-text-chunk` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[png-raw-profile-text-chunk]] and [[libfuzzer-graphicsmagick-coder-png]].

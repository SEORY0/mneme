---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Raw Camera With Fuzzer Controls Seed Mutate Buffered Scanf Overrun Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "raw-camera-with-fuzzer-controls"
harness_convention: "honggfuzz-fuzzed-data-provider"
vuln_class: "buffered-scanf-overrun"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "raw-camera-with-fuzzer-controls", "honggfuzz-fuzzed-data-provider", "seed-mutate", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "raw-camera-with-fuzzer-controls", "honggfuzz-fuzzed-data-provider", "buffered-scanf-overrun", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached No Target Crash Raw Camera With Fuzzer Controls Seed Mutate Buffered Scanf Overrun Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-camera-with-fuzzer-controls]]
- related harness facts: [[honggfuzz-fuzzed-data-provider]]

## Failure Shape
Switching from a mismatched RAF seed to the CR2 seed corpus fixed the file-family gate, and placing scalar-control padding before the seed avoided truncating the camera payload. Several CR2 corpus seeds reached clean processing without the target crash. The remaining gap is a medium-format metadata record whose textual numeric field is scanned from the in-memory datastream near a buffer boundary.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `raw-camera-with-fuzzer-controls` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_no_target_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The library payload is a raw camera file, but the fuzzer also consumes scalar image-processing controls before passing the remaining bytes to LibRaw. The target overrun is in textual metadata parsing where numeric fields are scanned from an in-memory buffer.

## Harness Contract
The target consumes fuzz bytes through a FuzzedDataProvider-like control phase, then passes the remaining byte span to LibRaw open_buffer, unpack, and multiple processing modes. Candidate layout matters: control bytes must be arranged so the remaining span still begins with a valid raw-camera file.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 5 attempts.
- Scope: generator repair and basin avoidance only.

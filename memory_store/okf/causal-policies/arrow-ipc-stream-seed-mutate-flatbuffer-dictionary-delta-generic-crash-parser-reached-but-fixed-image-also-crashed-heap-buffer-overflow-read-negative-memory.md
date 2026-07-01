---
type: negative-memory
title: "Arrow Ipc Stream Seed Mutate Flatbuffer Dictionary Delta Generic Crash Parser Reached But Fixed Image Also Crashed Heap Buffer Overflow Read Negative Memory"
description: "Round 36 negative memory for generic_crash with verifier signal parser_reached_but_fixed_image_also_crashed."
failure_class: "generic_crash"
verifier_signal: "parser_reached_but_fixed_image_also_crashed"
candidate_family: "seed_mutate_flatbuffer_dictionary_delta"
input_format: "arrow-ipc-stream"
harness_convention: "afl-libfuzzer-ipc-stream-reader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-but-fixed-image-also-crashed", "arrow-ipc-stream", "afl-libfuzzer-ipc-stream-reader", "seed-mutate-flatbuffer-dictionary-delta", "heap-buffer-overflow-read", "negative-memory", "round-36"]
match_keys: ["generic_crash", "parser_reached_but_fixed_image_also_crashed", "arrow-ipc-stream", "afl-libfuzzer-ipc-stream-reader", "heap-buffer-overflow-read", "generic-crash", "parser-reached-but-fixed-image-also-crashed", "negative_memory", "seed_mutate_flatbuffer_dictionary_delta", "seed-mutate-flatbuffer-dictionary-delta"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Arrow Ipc Stream Seed Mutate Flatbuffer Dictionary Delta Generic Crash Parser Reached But Fixed Image Also Crashed Heap Buffer Overflow Read Negative Memory

- key: `generic_crash x parser_reached_but_fixed_image_also_crashed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[arrow-ipc-stream]]
- related harness facts: [[afl-libfuzzer-ipc-stream-reader]]

## Failure Shape
A valid nested-dictionary Arrow IPC stream was a good parser carrier, and targeted FlatBuffer rewrites could mark later dictionary batches as deltas so the reader reached the dictionary-delta concatenation path. The successful local crashes were over-broad: the fixed image also aborted because the delta dictionary data still contained unresolved nested dictionary children, so construction or validation failed before a vulnerable-only arbitrary-read relation was isolated. Simple generated dictionary-delta streams and replayed IPC crash seeds stayed clean.

## Observed Basin
- Failure trajectory classes: no_crash, generic_crash, post_patch_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `generic_crash x parser_reached_but_fixed_image_also_crashed` on `arrow-ipc-stream` under `afl-libfuzzer-ipc-stream-reader` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_but_fixed_image_also_crashed` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_but_fixed_image_also_crashed`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 16 attempts.
- Scope: generator repair and basin avoidance only.

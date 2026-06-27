---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Blosc2 Frame Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "blosc2-frame"
harness_convention: "libfuzzer-afl"
vuln_class: "integer-overflow-to-out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "blosc2-frame", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "blosc2-frame", "libfuzzer-afl", "integer-overflow-to-out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached No Target Crash Blosc2 Frame Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[blosc2-frame]]
- related harness facts: [[libfuzzer-afl]]

## Failure Shape
- The available simple frame seeds had an empty metalayer index. Mutating the empty metalayer envelope
  alone did not produce a valid metalayer entry or reach the signed-offset dereference. A better seed
  needs at least one real metalayer index entry so only the serialized content offset has to be
  corrupted.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `blosc2-frame` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- A blosc2 frame starts with a msgpack-like frame header containing magic, header length, total frame
  length, sizes, codec/filter metadata, and a metalayer index envelope. The metalayer index maps names
  to signed serialized-value offsets, followed by serialized metalayer contents. Chunk-offset data and
  a trailer appear after the header and compressed chunks.

## Harness Contract
- The decompression-frame fuzzer feeds the raw input as an in-memory blosc2 super-chunk frame. If
  frame opening succeeds, it allocates an output buffer from the frame metadata and decompresses
  chunks in order. There is no harness-level byte carving or mode selector.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

---
type: "negative-memory"
title: "C Blosc2 Frame Seed Mutate No Crash Frame Metadata Reached Offset Sink Not Crashing Signed Integer Overflow Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal frame_metadata_reached_offset_sink_not_crashing."
failure_class: "no_crash"
verifier_signal: "frame_metadata_reached_offset_sink_not_crashing"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "afl-libfuzzer-compatible-whole-buffer-frame-decompressor"
vuln_class: "signed-integer-overflow"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "frame-metadata-reached-offset-sink-not-crashing", "c-blosc2-frame", "afl-libfuzzer-compatible-whole-buffer-frame-decompressor", "seed-mutate", "signed-integer-overflow", "negative-memory", "round-38"]
match_keys: ["no_crash", "frame_metadata_reached_offset_sink_not_crashing", "c-blosc2-frame", "afl-libfuzzer-compatible-whole-buffer-frame-decompressor", "signed-integer-overflow", "negative-memory", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# C Blosc2 Frame Seed Mutate No Crash Frame Metadata Reached Offset Sink Not Crashing Signed Integer Overflow Negative Memory

- key: `no_crash x frame_metadata_reached_offset_sink_not_crashing`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[afl-libfuzzer-compatible-whole-buffer-frame-decompressor]]

## Failure Shape
A valid frame seed could be made to parse with an extreme compressed-data length, and the frame metadata showed the intended header and size relation. Under this ASAN-oriented runner the signed-overflow-only path returned cleanly rather than aborting; variants targeting the later bounds addition, the task-text header-length relation, and every in-repo frame seed also exited cleanly. The likely blocker is that this build does not turn the signed overflow in the offset-position arithmetic into a nonzero sanitizer exit, and the subsequent negative wrapped value is caught by the existing boundary check before an invalid pointer is dereferenced.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x frame_metadata_reached_offset_sink_not_crashing` on `[[c-blosc2-frame]]` under `[[afl-libfuzzer-compatible-whole-buffer-frame-decompressor]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `frame_metadata_reached_offset_sink_not_crashing` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `frame_metadata_reached_offset_sink_not_crashing`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 9 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and basin avoidance only.

---
type: causal-policy
title: "No Crash Parser Rejected Or Clean Exit Audio Container Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_rejected_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_rejected_or_clean_exit"
candidate_family: "construct"
input_format: "audio-container"
harness_convention: "libfuzzer-virtual-io"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-rejected-or-clean-exit", "audio-container", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_rejected_or_clean_exit", "audio-container", "libfuzzer-virtual-io", "integer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Rejected Or Clean Exit Audio Container Negative Memory

- key: `no_crash x parser_rejected_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[audio-container]]
- related harness facts: [[libfuzzer-virtual-io]]

## Failure Shape
- RIFF/WAVE, RF64-like, CAF-like, AIFF-like, and AU-like containers with extreme channel or samplerate
  fields did not produce the target behavior. The likely missing condition is a format parser that
  stores larger SF_INFO values without clamping before the harness allocation/read path.

## Policy
Treat `no_crash x parser_rejected_or_clean_exit` on `audio-container` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The libsndfile front end autodetects several audio containers from raw file magic. Common PCM
  containers carry channel count, samplerate, frame sizing, and data chunks in their own endian/layout
  conventions. WAV-style channel count is limited by its field width, so formats with wider channel
  metadata may be more promising for this class.

## Harness Contract
- The fuzz target exposes the raw input through libsndfile virtual I/O and calls sf_open_virtual.
  After open it rejects zero or extremely large channel counts, allocates a float buffer proportional
  to channels, and reads frames. No FuzzedDataProvider carving or leading mode byte is used.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_rejected_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

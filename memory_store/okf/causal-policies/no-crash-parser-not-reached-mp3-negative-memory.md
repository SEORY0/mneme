---
type: causal-policy
title: "No Crash Parser Not Reached Mp3 Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "mp3"
harness_convention: "file-cli"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "mp3", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_not_reached", "mp3", "file-cli", "global-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Not Reached Mp3 Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mp3]]
- related harness facts: [[file-cli]]

## Failure Shape
- Malformed MP3 headers with the reserved bitrate index were rejected by the file sniffer before the
  MP3 reframe filter was set up, even when preceded by a plausible valid frame or ID3-style envelope.
  A better candidate should start with enough valid MP3 frame structure for GPAC to select the MP3
  filter, then place the reserved bitrate-index frame later in the stream.

## Policy
Treat `no_crash x parser_not_reached` on `mp3` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- MP3 frame headers contain sync bits, MPEG version, layer, protection, bitrate index, sampling-rate
  index, padding, and channel mode. The bitrate index is a four-bit table selector; the all-ones value
  is reserved and can exceed a table with entries only for normal values.

## Harness Contract
- The generated runner invokes a GPAC command-line inspection path over the raw file. The bytes must
  be recognized as an MP3 input by GPAC's filter selection before the MP3 frame parser and bitrate
  lookup are reached; there is no libFuzzer byte carving.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

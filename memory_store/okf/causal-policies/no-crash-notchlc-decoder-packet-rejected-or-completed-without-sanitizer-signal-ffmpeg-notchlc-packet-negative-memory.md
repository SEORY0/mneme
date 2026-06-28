---
type: causal-policy
title: "No Crash Notchlc Decoder Packet Rejected Or Completed Without Sanitizer Signal Ffmpeg Notchlc Packet Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal notchlc_decoder_packet_rejected_or_completed_without_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "notchlc_decoder_packet_rejected_or_completed_without_sanitizer_signal"
candidate_family: "construct"
input_format: "ffmpeg-notchlc-packet"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "notchlc-decoder-packet-rejected-or-completed-without-sanitizer-signal", "ffmpeg-notchlc-packet", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "notchlc-decoder-packet-rejected-or-completed-without-sanitizer-signal", "ffmpeg-notchlc-packet", "libfuzzer", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Notchlc Decoder Packet Rejected Or Completed Without Sanitizer Signal Ffmpeg Notchlc Packet Negative Memory

- key: `no_crash x notchlc_decoder_packet_rejected_or_completed_without_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-notchlc-packet]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Minimal raw NotchLC frames with coherent block metadata and intentionally short UV sub-block data did not produce the expected uninitialized-read signal.
- The candidates targeted branch-specific reads that lack explicit byte-left checks, but either the packet was rejected before those reads became observable or FFmpeg's byte-reader padding avoided a sanitizer-visible uninitialized value.

## Policy
Treat `no_crash x notchlc_decoder_packet_rejected_or_completed_without_sanitizer_signal` on `ffmpeg-notchlc-packet` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `notchlc_decoder_packet_rejected_or_completed_without_sanitizer_signal`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[ffmpeg-notchlc-packet]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x notchlc_decoder_packet_rejected_or_completed_without_sanitizer_signal`.
- Candidate family: `construct`.
- Basin summary: Minimal raw NotchLC frames with coherent block metadata and intentionally short UV sub-block data did not produce the expected uninitialized-read signal.

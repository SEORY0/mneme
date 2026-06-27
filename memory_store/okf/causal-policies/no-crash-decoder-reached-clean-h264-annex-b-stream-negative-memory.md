---
type: causal-policy
title: "No Crash Decoder Reached Clean H264 Annex B Stream Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal decoder_reached_clean."
failure_class: "no_crash"
verifier_signal: "decoder_reached_clean"
candidate_family: "seed_mutate"
input_format: "h264 annex-b stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "decoder-reached-clean", "h264-annex-b-stream", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "decoder-reached-clean", "h264-annex-b-stream", "libfuzzer", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Decoder Reached Clean H264 Annex B Stream Negative Memory

- key: `no_crash x decoder_reached_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h264-annex-b-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A bundled raw H.264 seed reached the decoder and decoded frames.
- A reduced stream preserving parameter sets plus truncated slice data still decoded cleanly, so the missing-slice uninitialized path was not triggered.

## Policy
Treat `no_crash x decoder_reached_clean` on `h264 annex-b stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_reached_clean`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[h264-annex-b-stream]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x decoder_reached_clean`.
- Candidate family: `seed_mutate`.
- Basin summary: A bundled raw H.264 seed reached the decoder and decoded frames.

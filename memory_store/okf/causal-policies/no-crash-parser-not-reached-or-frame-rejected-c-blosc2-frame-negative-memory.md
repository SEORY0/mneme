---
type: causal-policy
title: "No Crash Parser Not Reached Or Frame Rejected C Blosc2 Frame Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_not_reached_or_frame_rejected."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_frame_rejected"
candidate_family: "seed_mutate"
input_format: "c-blosc2-frame"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-frame-rejected", "c-blosc2-frame", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_not_reached_or_frame_rejected", "c-blosc2-frame", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Not Reached Or Frame Rejected C Blosc2 Frame Negative Memory

- key: `no_crash x parser_not_reached_or_frame_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Seed-preserving mutations of header metalayer index metadata and trailer extent metadata stayed clean or were rejected before the vulnerable copy. The likely missing condition is preserving super-chunk construction while placing a metadata content pointer and declared content span in the vulnerable header-copy relation.

## Policy
Treat `no_crash x parser_not_reached_or_frame_rejected` on `c-blosc2-frame` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached_or_frame_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
A c-blosc2 frame has an accepted frame header, declared frame length, compressed chunk metadata, chunk payloads, and optional header and trailer metalayer metadata encoded with msgpack-like markers. The header metalayer index maps names to declared content locations, and the vulnerable reader accounts for one cursor while copying from a separate declared content location.

## Harness Contract
The libFuzzer target passes the raw input buffer directly to blosc2_schunk_from_buffer, then attempts frame decompression. Valid seed frames from the in-repo corpus reach the frame parser; broad outer-frame corruption tends to stop before metalayer access.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_not_reached_or_frame_rejected`
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
Seed-preserving mutations of header metalayer index metadata and trailer extent metadata stayed clean or were rejected before the vulnerable copy. The likely missing condition is preserving super-chunk construction while placing a metadata content pointer and declared content span in the vulnerable header-copy relation.

### Format Contract Delta
A c-blosc2 frame has an accepted frame header, declared frame length, compressed chunk metadata, chunk payloads, and optional header and trailer metalayer metadata encoded with msgpack-like markers. The header metalayer index maps names to declared content locations, and the vulnerable reader accounts for one cursor while copying from a separate declared content location.

### Harness Contract Delta
The libFuzzer target passes the raw input buffer directly to blosc2_schunk_from_buffer, then attempts frame decompression. Valid seed frames from the in-repo corpus reach the frame parser; broad outer-frame corruption tends to stop before metalayer access.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

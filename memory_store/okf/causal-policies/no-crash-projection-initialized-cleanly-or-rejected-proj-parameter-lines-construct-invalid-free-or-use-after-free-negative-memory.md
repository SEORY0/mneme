---
type: negative-memory
title: "No Crash Projection Initialized Cleanly Or Rejected Proj Parameter Lines Construct Invalid Free Or Use After Free Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal projection_initialized_cleanly_or_rejected."
failure_class: "no_crash"
verifier_signal: "projection_initialized_cleanly_or_rejected"
candidate_family: "construct"
input_format: "proj-parameter-lines"
harness_convention: "libfuzzer"
vuln_class: "invalid-free-or-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "projection-initialized-cleanly-or-rejected", "proj-parameter-lines", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "projection_initialized_cleanly_or_rejected", "proj-parameter-lines", "libfuzzer", "invalid-free-or-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Projection Initialized Cleanly Or Rejected Proj Parameter Lines Construct Invalid Free Or Use After Free Negative Memory

- key: `no_crash x projection_initialized_cleanly_or_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[proj-parameter-lines]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid three-line PROJ inputs using geostationary projection parameters and sweep-axis selection executed cleanly. The attempted variants did not reach a cleanup path where the sweep-axis member caused a sanitizer-visible invalid free.

## Policy
Treat `no_crash x projection_initialized_cleanly_or_rejected` on `proj-parameter-lines` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `projection_initialized_cleanly_or_rejected` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `projection_initialized_cleanly_or_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The standard PROJ fuzz input is three newline-separated fields: source projection definition, destination projection definition, and coordinates. Projection definitions are plus-prefixed parameter strings parsed by pj_init_plus.

## Harness Contract
libFuzzer raw bytes are copied into a NUL-terminated buffer, split on the first two newlines, parsed as two projections, then transformed using either textual or binary coordinates if both projections initialize.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.

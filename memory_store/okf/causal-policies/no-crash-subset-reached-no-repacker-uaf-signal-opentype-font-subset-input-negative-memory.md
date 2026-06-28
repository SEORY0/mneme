---
type: causal-policy
title: "No Crash Subset Reached No Repacker Uaf Signal Opentype Font Subset Input Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal subset_reached_no_repacker_uaf_signal."
failure_class: "no_crash"
verifier_signal: "subset_reached_no_repacker_uaf_signal"
candidate_family: "seed_replay_and_trailer_mutation"
input_format: "opentype-font-subset-input"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "subset-reached-no-repacker-uaf-signal", "opentype-font-subset-input", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "subset-reached-no-repacker-uaf-signal", "opentype-font-subset-input", "libfuzzer", "heap-use-after-free", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Subset Reached No Repacker Uaf Signal Opentype Font Subset Input Negative Memory

- key: `no_crash x subset_reached_no_repacker_uaf_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font-subset-input]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Valid subset-oriented OpenType and TrueType seeds, including variable, color, CFF-like, and layout-heavy fonts, were accepted by the subset fuzzer but did not trigger the repacker overflow-record dangling-reference condition.
- The missing ingredient is likely a font table graph that forces repacker overflow resolution and vector growth while preserving links that later need patching.

## Policy
Treat `no_crash x subset_reached_no_repacker_uaf_signal` on `opentype-font-subset-input` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `subset_reached_no_repacker_uaf_signal`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[opentype-font-subset-input]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x subset_reached_no_repacker_uaf_signal`.
- Candidate family: `seed_replay_and_trailer_mutation`.
- Basin summary: Valid subset-oriented OpenType and TrueType seeds, including variable, color, CFF-like, and layout-heavy fonts, were accepted by the subset fuzzer but did not trigger the repacker overflow-record dangling-reference condition.

---
type: causal-policy
title: "No Crash Seed Decoded Target Header Not Reached One Unconfirmed Non Target Crash Fuji RAF Raw Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal seed_decoded_target_header_not_reached_one_unconfirmed_non_target_crash."
failure_class: "no_crash"
verifier_signal: "seed_decoded_target_header_not_reached_one_unconfirmed_non_target_crash"
candidate_family: "seed_mutate"
input_format: "fuji-raf/raw"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "seed-decoded-target-header-not-reached-one-unconfirmed-non-target-crash", "fuji-raf-raw", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "seed-decoded-target-header-not-reached-one-unconfirmed-non-target-crash", "fuji-raf-raw", "libfuzzer", "uninitialized-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Seed Decoded Target Header Not Reached One Unconfirmed Non Target Crash Fuji RAF Raw Negative Memory

- key: `no_crash x seed_decoded_target_header_not_reached_one_unconfirmed_non_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fuji-raf-raw]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Full and truncated Fuji RAF seeds, neutral configuration tails, marker-tail mutations, and a synthetic RAF marker did not produce a confirmed target match.
- One truncated-seed variant gave an unconfirmed generic crash/dirty confirm behavior and then reran as clean, so it was not submitted as a solve.
- The remaining gap is a Fuji compressed RAW sample or metadata mutation that sets the raw-data offset to a short header region so the compressed header parser observes EOF while still accepting the image container.

## Policy
Treat `no_crash x seed_decoded_target_header_not_reached_one_unconfirmed_non_target_crash` on `fuji-raf/raw` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `seed_decoded_target_header_not_reached_one_unconfirmed_non_target_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[fuji-raf-raw]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x seed_decoded_target_header_not_reached_one_unconfirmed_non_target_crash`.
- Candidate family: `seed_mutate`.
- Basin summary: Full and truncated Fuji RAF seeds, neutral configuration tails, marker-tail mutations, and a synthetic RAF marker did not produce a confirmed target match.

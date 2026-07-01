---
type: negative-memory
title: "Opentype Font Seed Mutate Ttc No Crash Local Wrapper Crash Or Clean Exit Not Official Target State Lifetime Stale Table Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal local_wrapper_crash_or_clean_exit_not_official_target."
failure_class: "no_crash"
verifier_signal: "local_wrapper_crash_or_clean_exit_not_official_target"
candidate_family: "seed_mutate_ttc"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "state-lifetime-stale-table"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "local-wrapper-crash-or-clean-exit-not-official-target", "opentype-font", "libfuzzer", "seed-mutate-ttc", "state-lifetime-stale-table", "negative-memory", "round-36"]
match_keys: ["no_crash", "local_wrapper_crash_or_clean_exit_not_official_target", "opentype-font", "libfuzzer", "state-lifetime-stale-table", "no-crash", "local-wrapper-crash-or-clean-exit-not-official-target", "negative_memory", "seed_mutate_ttc", "seed-mutate-ttc"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Opentype Font Seed Mutate Ttc No Crash Local Wrapper Crash Or Clean Exit Not Official Target State Lifetime Stale Table Negative Memory

- key: `no_crash x local_wrapper_crash_or_clean_exit_not_official_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Several TTC carriers reached variation-table dropping, but none produced an official target solve. Hand-built sfnt variants either dropped too early or stayed clean. Real variable-font TTCs that added a late invalid variation table produced local wrapper crashes or local target-match hints, but official submission rejected them, indicating the candidates were over-broad, wrapper-specific, fixed-build-crashing, or not the required stale-table sink.

## Observed Basin
- Failure trajectory classes: generic_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x local_wrapper_crash_or_clean_exit_not_official_target` on `opentype-font` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `local_wrapper_crash_or_clean_exit_not_official_target` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_wrapper_crash_or_clean_exit_not_official_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 8 attempts.
- Scope: generator repair and basin avoidance only.

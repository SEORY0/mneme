---
type: causal-policy
title: "No Crash Selected Harness Did Not Reach Cgats Loader Lcms Cgats Or Icc Transform Harness Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal selected_harness_did_not_reach_cgats_loader."
failure_class: "no_crash"
verifier_signal: "selected_harness_did_not_reach_cgats_loader"
candidate_family: "construct"
input_format: "lcms-cgats-or-icc-transform-harness"
harness_convention: "libfuzzer"
vuln_class: "invalid-character-parser-acceptance"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "selected-harness-did-not-reach-cgats-loader", "lcms-cgats-or-icc-transform-harness", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "selected-harness-did-not-reach-cgats-loader", "lcms-cgats-or-icc-transform-harness", "libfuzzer", "invalid-character-parser-acceptance", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Selected Harness Did Not Reach Cgats Loader Lcms Cgats Or Icc Transform Harness Negative Memory

- key: `no_crash x selected_harness_did_not_reach_cgats_loader`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[lcms-cgats-or-icc-transform-harness]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- CGATS text candidates with valid section structure and intentionally invalid characters did not reach the described loader in local verification.
- The observed executable consumed the input as a universal ICC transform test, so the text CGATS grammar was not the active parser path for the verifier run.

## Policy
Treat `no_crash x selected_harness_did_not_reach_cgats_loader` on `lcms-cgats-or-icc-transform-harness` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `selected_harness_did_not_reach_cgats_loader`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[lcms-cgats-or-icc-transform-harness]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x selected_harness_did_not_reach_cgats_loader`.
- Candidate family: `construct`.
- Basin summary: CGATS text candidates with valid section structure and intentionally invalid characters did not reach the described loader in local verification.

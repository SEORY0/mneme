---
type: causal-policy
title: "No Crash Harness Mismatch TIFF Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal harness_mismatch."
failure_class: "no_crash"
verifier_signal: "harness_mismatch"
candidate_family: "seed_mutate"
input_format: "tiff"
harness_convention: "libfuzzer"
vuln_class: "improper-error-handling"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "harness-mismatch", "tiff", "libfuzzer", "negative-memory", "round-18"]
match_keys: ["no-crash", "harness-mismatch", "tiff", "libfuzzer", "improper-error-handling", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Harness Mismatch TIFF Negative Memory

- key: `no_crash x harness_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tiff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A tiled compressed TIFF seed was mutated to make the raw tile read fail while preserving the TIFF directory, but local verify ran a matrix-save buffer fuzzer rather than a TIFF load path, so the described tiffload relation was not exercised.

## Policy
Treat `no_crash x harness_mismatch` on `tiff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `harness_mismatch`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[tiff]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x harness_mismatch`.
- Candidate family: `seed_mutate`.
- Basin summary: A tiled compressed TIFF seed was mutated to make the raw tile read fail while preserving the TIFF directory, but local verify ran a matrix-save buffer fuzzer rather than a TIFF load path, so the described tiffload relation was not exercised.

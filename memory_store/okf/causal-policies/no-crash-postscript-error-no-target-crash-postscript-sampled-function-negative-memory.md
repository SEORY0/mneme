---
type: causal-policy
title: "No Crash Postscript Error No Target Crash Postscript Sampled Function Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal postscript_error_no_target_crash."
failure_class: "no_crash"
verifier_signal: "postscript_error_no_target_crash"
candidate_family: "construct"
input_format: "postscript-sampled-function"
harness_convention: "libfuzzer-ghostscript-gstoraster"
vuln_class: "postscript-execution-stack-cleanup"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "postscript-error-no-target-crash", "postscript-sampled-function", "libfuzzer-ghostscript-gstoraster", "negative-memory", "round-18"]
match_keys: ["no-crash", "postscript-error-no-target-crash", "postscript-sampled-function", "libfuzzer-ghostscript-gstoraster", "postscript-execution-stack-cleanup", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Postscript Error No Target Crash Postscript Sampled Function Negative Memory

- key: `no_crash x postscript_error_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-sampled-function]]
- related harness facts: [[libfuzzer-ghostscript-gstoraster]]

## Failure Shape
- A sampled-function-oriented PostScript probe produced a normal interpreter error path but did not leave the execution stack in the vulnerable completion-routine state.

## Policy
Treat `no_crash x postscript_error_no_target_crash` on `postscript-sampled-function` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `postscript_error_no_target_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[postscript-sampled-function]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ghostscript-gstoraster]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x postscript_error_no_target_crash`.
- Candidate family: `construct`.
- Basin summary: A sampled-function-oriented PostScript probe produced a normal interpreter error path but did not leave the execution stack in the vulnerable completion-routine state.

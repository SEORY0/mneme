---
type: causal-policy
title: "No Crash Avcbin Opened Seed No Target Crash Avcbin Tar Coverage Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal avcbin_opened_seed_no_target_crash."
failure_class: "no_crash"
verifier_signal: "avcbin_opened_seed_no_target_crash"
candidate_family: "seed_mutate"
input_format: "avcbin-tar-coverage"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "avcbin-opened-seed-no-target-crash", "avcbin-tar-coverage", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["no-crash", "avcbin-opened-seed-no-target-crash", "avcbin-tar-coverage", "libfuzzer", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Avcbin Opened Seed No Target Crash Avcbin Tar Coverage Negative Memory

- key: `no_crash x avcbin_opened_seed_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[avcbin-tar-coverage]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The extracted source included unrelated netCDF patches, but the verifier binary was AVCBIN.
- A valid tar-wrapped AVC coverage seed opened without crashing; no successful mutation of coverage index records was completed in this pass.

## Policy
Treat `no_crash x avcbin_opened_seed_no_target_crash` on `avcbin-tar-coverage` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `avcbin_opened_seed_no_target_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[avcbin-tar-coverage]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

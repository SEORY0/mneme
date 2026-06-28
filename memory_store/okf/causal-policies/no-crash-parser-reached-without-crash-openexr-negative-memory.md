---
type: causal-policy
title: "No Crash Parser Reached Without Crash Openexr Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal parser_reached_without_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_without_crash"
candidate_family: "seed_mutate"
input_format: "openexr"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-without-crash", "openexr", "libfuzzer", "negative-memory", "round-17"]
match_keys: ["no-crash", "parser-reached-without-crash", "openexr", "libfuzzer", "integer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Parser Reached Without Crash Openexr Negative Memory

- key: `no_crash x parser_reached_without_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openexr]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Real EXR seeds with mutated chunk-table offsets did not trigger the overflow read.
- The likely missing condition is a chunk metadata combination that causes the core in-memory stream to request a nonzero size at a wrapped high offset while bypassing earlier C++ stream range checks.

## Policy
Treat `no_crash x parser_reached_without_crash` on `openexr` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_without_crash`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[openexr]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

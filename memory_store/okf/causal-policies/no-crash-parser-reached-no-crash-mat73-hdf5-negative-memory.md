---
type: causal-policy
title: "No Crash Parser Reached No Crash Mat73 Hdf5 Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_no_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_crash"
candidate_family: "seed_mutate"
input_format: "mat73-hdf5"
harness_convention: "libfuzzer"
vuln_class: "bad-api-argument"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-crash", "mat73-hdf5", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_no_crash", "mat73-hdf5", "libfuzzer", "bad-api-argument", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached No Crash Mat73 Hdf5 Negative Memory

- key: `no_crash x parser_reached_no_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mat73-hdf5]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Real MAT73/HDF5 seeds reached the parser, but mutations to class attributes, dataset names, and metadata strings were either ignored or rejected before the bad dimension call. The missing gate is likely a valid HDF5 object layout whose dataspace rank and MATLAB class metadata disagree while still being accepted as a variable.

## Policy
Treat `no_crash x parser_reached_no_crash` on `mat73-hdf5` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
MAT version 7.3 files are HDF5 containers with MATLAB-specific attributes and datasets. Variable iteration opens HDF5 links, reads MATLAB class/type metadata, obtains dataspaces, and asks HDF5 for simple extent dimensions into buffers sized from the interpreted rank or object kind.

## Harness Contract
The matio fuzzer writes the raw input to a temporary file, opens it as a MAT file, then iterates variable info and variable data. There is no harness prefix; HDF5 validity and MATLAB metadata drive reachability.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

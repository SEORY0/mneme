---
type: causal-policy
title: "No Crash Hdf5 Open Clean Hdf5 File Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal hdf5_open_clean."
failure_class: "no_crash"
verifier_signal: "hdf5_open_clean"
candidate_family: "seed_mutate"
input_format: "hdf5-file"
harness_convention: "libfuzzer-carved-file"
vuln_class: "out-of-bounds-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "hdf5-open-clean", "hdf5-file", "negative-memory", "round-7"]
match_keys: ["no_crash", "hdf5_open_clean", "hdf5-file", "libfuzzer-carved-file", "out-of-bounds-access", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Hdf5 Open Clean Hdf5 File Negative Memory

- key: `no_crash x hdf5_open_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[hdf5-file]]
- related harness facts: [[libfuzzer-carved-file]]

## Failure Shape
A valid HDF5 sample with the harness selector prefix opened cleanly. The target in address decoding
likely needs malformed low-level file metadata controlling encoded address length or undefined-
address handling, which was not changed in the seed.

## Policy
Treat `no_crash x hdf5_open_clean` on `hdf5-file` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `hdf5_open_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
HDF5 files contain a signature, superblock, size/address-size metadata, object headers, heaps,
B-trees, and encoded file addresses. The target address decoder reads an address field byte-by-byte
using an address length derived from file metadata.

## Harness Contract
The libFuzzer target consumes the first input byte as a selector, writes the remaining bytes to a
temporary file, and opens that file with H5Fopen. In this build the selector condition always takes
the H5Fopen branch.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.

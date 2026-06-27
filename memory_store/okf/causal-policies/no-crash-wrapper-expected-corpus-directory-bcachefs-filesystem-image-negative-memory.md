---
type: causal-policy
title: "No Crash Wrapper Expected Corpus Directory Bcachefs Filesystem Image Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal wrapper_expected_corpus_directory."
failure_class: "no_crash"
verifier_signal: "wrapper_expected_corpus_directory"
candidate_family: "construct"
input_format: "bcachefs-filesystem-image"
harness_convention: "libfuzzer-directory-wrapper"
vuln_class: "integer-overflow-or-pointer-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-expected-corpus-directory", "bcachefs-filesystem-image", "negative-memory", "round-13"]
match_keys: ["no_crash", "wrapper_expected_corpus_directory", "bcachefs-filesystem-image", "libfuzzer-directory-wrapper", "integer-overflow-or-pointer-bounds", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Wrapper Expected Corpus Directory Bcachefs Filesystem Image Negative Memory

- key: `no_crash x wrapper_expected_corpus_directory`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[bcachefs-filesystem-image]]
- related harness facts: [[libfuzzer-directory-wrapper]]

## Failure Shape
A constructed bcachefs-like superblock file did not execute under the intended single-file contract because the selected container wrapper invokes the libFuzzer binary with a directory path. I inspected the container wrapper and confirmed this surface mismatch; the remaining blocker is adapting a single submitted file to a wrapper that expects a corpus directory.

## Policy
Treat `no_crash x wrapper_expected_corpus_directory` on `bcachefs-filesystem-image` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_expected_corpus_directory`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The bcachefs probe looks for bcache/bcachefs magic at the filesystem superblock location, validates a superblock offset field, checks device index versus device count, computes the superblock size from a u64-count field, and walks typed superblock fields. Members fields contain an array of device records used for UUID and size calculation.

## Harness Contract
The container's /bin/arvo invokes the blkid libFuzzer target with a fixed /tmp/poc path as a corpus directory rather than passing a single input file. When /tmp/poc is a regular file, the target exits with a required-directory message before processing the constructed bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x wrapper_expected_corpus_directory`
- related format facts: [[bcachefs-filesystem-image]]
- related harness facts: [[libfuzzer-directory-wrapper]]

### Failure Shape Delta
A constructed bcachefs-like superblock file did not execute under the intended single-file contract because the selected container wrapper invokes the libFuzzer binary with a directory path. I inspected the container wrapper and confirmed this surface mismatch; the remaining blocker is adapting a single submitted file to a wrapper that expects a corpus directory.

### Format Contract Delta
The bcachefs probe looks for bcache/bcachefs magic at the filesystem superblock location, validates a superblock offset field, checks device index versus device count, computes the superblock size from a u64-count field, and walks typed superblock fields. Members fields contain an array of device records used for UUID and size calculation.

### Harness Contract Delta
The container's /bin/arvo invokes the blkid libFuzzer target with a fixed /tmp/poc path as a corpus directory rather than passing a single input file. When /tmp/poc is a regular file, the target exits with a required-directory message before processing the constructed bytes.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.

---
type: causal-policy
title: "No Crash Bcachefs Filesystem Image Wrapper Expected Corpus Directory Negative Memory"
description: "Negative memory for no_crash with wrapper_expected_corpus_directory on bcachefs-filesystem-image inputs."
failure_class: no_crash
verifier_signal: wrapper_expected_corpus_directory
candidate_family: construct
input_format: bcachefs-filesystem-image
harness_convention: libfuzzer-directory-wrapper
vuln_class: integer-overflow-or-pointer-bounds
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, wrapper-expected-corpus-directory, bcachefs-filesystem-image, integer-overflow-or-pointer-bounds, negative_memory]
match_keys: [no-crash, wrapper-expected-corpus-directory, bcachefs-filesystem-image, integer-overflow-or-pointer-bounds]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Bcachefs Filesystem Image Wrapper Expected Corpus Directory Negative Memory

- key: `no_crash x wrapper_expected_corpus_directory`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[bcachefs-filesystem-image]]

## Dead End
A constructed bcachefs-like superblock file did not execute under the intended single-file contract because the selected container wrapper invokes the libFuzzer binary with a directory path. I inspected the container wrapper and confirmed this surface mismatch; the remaining blocker is adapting a single submitted file to a wrapper that expects a corpus directory.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.

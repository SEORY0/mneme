---
type: causal-policy
title: "No Crash Xaac Encoder Fdp Runner Wrapper Requires Corpus Directory Negative Memory"
description: "Negative memory for no_crash with runner_wrapper_requires_corpus_directory on xaac-encoder-fdp inputs."
failure_class: no_crash
verifier_signal: runner_wrapper_requires_corpus_directory
candidate_family: construct
input_format: xaac-encoder-fdp
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-write
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, runner-wrapper-requires-corpus-directory, xaac-encoder-fdp, heap-buffer-overflow-write, negative_memory]
match_keys: [no-crash, runner-wrapper-requires-corpus-directory, xaac-encoder-fdp, heap-buffer-overflow-write]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Xaac Encoder Fdp Runner Wrapper Requires Corpus Directory Negative Memory

- key: `no_crash x runner_wrapper_requires_corpus_directory`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[xaac-encoder-fdp]]

## Dead End
The encoder source harness consumes FuzzedDataProvider configuration followed by synthetic audio payload, but the arvo wrapper invokes libFuzzer in corpus-directory mode. The runner copies a single file to the fixed input path, so the image reports that the required corpus directory is absent before executing candidate bytes.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.

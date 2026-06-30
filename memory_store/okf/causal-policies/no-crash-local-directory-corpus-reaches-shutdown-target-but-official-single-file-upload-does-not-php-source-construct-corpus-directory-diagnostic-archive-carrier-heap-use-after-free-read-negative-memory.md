---
type: negative-memory
title: "No Crash Local Directory Corpus Reaches Shutdown Target But Official Single File Upload Does Not Php Source Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal local_directory_corpus_reaches_shutdown_target_but_official_single_file_upload_does_not."
failure_class: "no_crash"
verifier_signal: "local_directory_corpus_reaches_shutdown_target_but_official_single_file_upload_does_not"
candidate_family: "construct|corpus_directory_diagnostic|archive_carrier"
input_format: "php-source"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-directory-corpus-reaches-shutdown-target-but-official-single-file-upload-does-not", "php-source", "libfuzzer", "construct-corpus-directory-diagnostic-archive-carrier", "heap-use-after-free-read", "negative-memory", "round-28"]
match_keys: ["no_crash", "local_directory_corpus_reaches_shutdown_target_but_official_single_file_upload_does_not", "php-source", "libfuzzer", "heap-use-after-free-read", "negative_memory", "construct", "use-after-free-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Local Directory Corpus Reaches Shutdown Target But Official Single File Upload Does Not Php Source Negative Memory

- key: `no_crash x local_directory_corpus_reaches_shutdown_target_but_official_single_file_upload_does_not`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[php-source]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Redefining disabled internal function names as userland functions can perturb the PHP function table and locally reaches the request-shutdown fast-cleanup bug when the fuzzer is given a corpus directory. The official submission path only accepts a single uploaded file, and archive carriers were not unpacked into a corpus directory, so the submitted candidates exited normally instead of exercising the target path.

## Policy
For `no_crash x local_directory_corpus_reaches_shutdown_target_but_official_single_file_upload_does_not` on `php-source`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `construct|corpus_directory_diagnostic|archive_carrier` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[php-source]]: The parser fuzzer consumes PHP source text and compiles it without executing normal application logic. The fuzzer SAPI starts a request with a hardcoded disabled-functions list, then shuts the request down, so source that redeclares names from that disabled set can affect the function table observed by shutdown cleanup.
- Harness [[libfuzzer]]: The local wrapper invokes the PHP parser libFuzzer binary on a fixed path. In local Docker verification, a directory at that path is treated as a corpus and its entries are processed; a regular file at that path is rejected before the fuzzer callback runs. The official submit endpoint uploads one regular file, not a directory.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.

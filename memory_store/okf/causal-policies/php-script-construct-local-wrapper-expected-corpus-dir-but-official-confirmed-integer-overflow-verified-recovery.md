---
type: causal-policy
title: "Php Script Construct Local Wrapper Expected Corpus Dir But Official Confirmed Integer Overflow Verified Recovery"
description: "Round 12 verified recovery for no_crash with verifier signal local_wrapper_expected_corpus_dir_but_official_confirmed."
failure_class: "no_crash"
verifier_signal: "local_wrapper_expected_corpus_dir_but_official_confirmed"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-wrapper-expected-corpus-dir-but-official-confirmed", "php-script", "verified-recovery", "round-12"]
match_keys: ["no_crash", "local_wrapper_expected_corpus_dir_but_official_confirmed", "php-script", "libfuzzer", "integer-overflow", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Php Script Construct Local Wrapper Expected Corpus Dir But Official Confirmed Integer Overflow Verified Recovery

- key: `no_crash x local_wrapper_expected_corpus_dir_but_official_confirmed`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[php-script]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `php-script` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `no_crash` with signal `local_wrapper_expected_corpus_dir_but_official_confirmed` on `php-script` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Feed raw PHP source to the execute fuzzer and call character range generation with ascending one-character bounds plus an overlarge integer step. The vulnerable character branch casts and applies the step without the same overlarge-step guard used by numeric ranges, producing the official vuln/fix split.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The payload is ordinary PHP source, not a serialized wrapper. It must include executable PHP code that reaches the standard library range function with string endpoints and a numeric step.

## Harness Contract
The execute fuzzer passes the raw input buffer as a PHP request body, ignores overly large source buffers, installs an execution-step budget, and executes the script. The local wrapper may mis-handle single-file verification as a corpus path, so official submit is the reliable signal for this task.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.

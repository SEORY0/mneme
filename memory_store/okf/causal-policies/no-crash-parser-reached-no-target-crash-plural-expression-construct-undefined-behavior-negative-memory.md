---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Plural Expression Construct Undefined Behavior Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "plural-expression"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "plural-expression", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "plural-expression", "libfuzzer", "undefined-behavior", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached No Target Crash Plural Expression Construct Undefined Behavior Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[plural-expression]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Invalid and exceptional plural expressions reached the fuzzer but did not reproducibly trigger the missing-return sanitizer condition from preserved candidate files.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `plural-expression` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_no_target_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is a Wt plural-expression string accepted by a C-like expression parser over variable n. Invalid syntax and unsafe arithmetic throw exceptions that are caught in the fuzz helper.

## Harness Contract
The fuzz target feeds raw bytes as a string when the input length is within the configured bounds, calls evalPluralCase with a fixed numeric value, catches parser/operation exceptions, and returns normally unless sanitizer instrumentation detects the helper falling through.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 4 attempts.
- Scope: generator repair and basin avoidance only.

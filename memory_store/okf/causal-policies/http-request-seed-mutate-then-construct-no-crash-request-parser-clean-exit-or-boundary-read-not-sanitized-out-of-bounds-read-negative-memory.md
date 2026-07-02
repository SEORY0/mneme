---
type: negative-memory
title: "Http Request Seed Mutate Then Construct No Crash Request Parser Clean Exit Or Boundary Read Not Sanitized Out Of Bounds Read Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal request_parser_clean_exit_or_boundary_read_not_sanitized."
failure_class: "no_crash"
verifier_signal: "request_parser_clean_exit_or_boundary_read_not_sanitized"
candidate_family: "seed_mutate_then_construct"
input_format: "http-request"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "request-parser-clean-exit-or-boundary-read-not-sanitized", "http-request", "libfuzzer", "seed-mutate-then-construct", "out-of-bounds-read", "negative-memory", "round-33"]
match_keys: ["no_crash", "request_parser_clean_exit_or_boundary_read_not_sanitized", "http-request", "libfuzzer", "seed-mutate-then-construct", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Http Request Seed Mutate Then Construct No Crash Request Parser Clean Exit Or Boundary Read Not Sanitized Out Of Bounds Read Negative Memory

- key: `no_crash x request_parser_clean_exit_or_boundary_read_not_sanitized`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[http-request]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Seed mutation and constructed requests reached ordinary request parsing but did not produce a sanitizer-visible crash. The likely vulnerable pattern is a logical header-boundary read in the fixed request buffer: satisfying the finalizer and placing known header prefixes near a request boundary still left the read inside the fuzz copy allocation or on benign delimiter bytes.

## Policy
Treat `no_crash x request_parser_clean_exit_or_boundary_read_not_sanitized` on `http-request` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `request_parser_clean_exit_or_boundary_read_not_sanitized`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `request_parser_clean_exit_or_boundary_read_not_sanitized`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[http-request]]. The input is an HTTP request: method, path, version, header lines, and a blank-line terminator. Known request headers are parsed by matching a short case-insensitive prefix first, then advancing over the expected full header name and checking for a name/value separator. Header discovery records line starts and ends in a fixed-size helper table before recognized headers are interpreted.

## Harness Contract
Use [[libfuzzer]]. The harness passes raw libFuzzer bytes directly to the request parser. It copies the bytes into a fixed static request buffer, truncates inputs that exceed that buffer, requires the request finalizer to observe a complete header terminator, and then parses using the full copied length rather than a separately saved end-of-headers pointer.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 14 attempts.
- Scope: generator repair and basin avoidance only.

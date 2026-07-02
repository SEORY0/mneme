---
type: negative-memory
title: "Http Request Construct No Crash Clean Exit No Sanitizer Signal No Sanitizer Signal From Short Header Parse Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal clean_exit_no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "clean_exit_no_sanitizer_signal"
candidate_family: "construct"
input_format: "http-request"
harness_convention: "libfuzzer"
vuln_class: "no-sanitizer-signal-from-short-header-parse"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "clean-exit-no-sanitizer-signal", "http-request", "libfuzzer", "construct", "no-sanitizer-signal-from-short-header-parse", "negative-memory", "round-33"]
match_keys: ["no_crash", "clean_exit_no_sanitizer_signal", "http-request", "libfuzzer", "construct", "no-sanitizer-signal-from-short-header-parse", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Http Request Construct No Crash Clean Exit No Sanitizer Signal No Sanitizer Signal From Short Header Parse Negative Memory

- key: `no_crash x clean_exit_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[http-request]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Syntactically valid HTTP requests reached the raw request-parser harness, but short and minimally truncated If-Modified-Since values did not produce a sanitizer-visible failure. Moving the undersized date value near the end of the fuzzer copy buffer and testing a separate many-header parser-capacity family also stayed in the clean-exit basin; official submission of the most plausible fixed-position date-read candidate reported no vulnerable crash.

## Policy
Treat `no_crash x clean_exit_no_sanitizer_signal` on `http-request` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `clean_exit_no_sanitizer_signal`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_no_sanitizer_signal`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[http-request]]. The input is a raw HTTP request: a request line with method, path, and HTTP version, followed by CRLF-delimited headers and a blank-line terminator. Header values are parsed by matching known header names and splitting at the line terminator. If-Modified-Since is expected to contain an RFC-style date string with fixed weekday, day, month, year, time, and GMT fields; malformed or short values can be recorded as a header value before the date parser rejects them.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer harness passes the entire raw file byte string directly to the Lwan HTTP request parser. There is no mode byte, no FuzzedDataProvider trailer, and no file wrapper. The harness copies input into an internal fixed request buffer, requires a complete CRLFCRLF-terminated request, then parses query, cookie, encoding, If-Modified-Since, and Range helper state.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 6 attempts.
- Scope: generator repair and basin avoidance only.

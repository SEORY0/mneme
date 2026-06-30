---
type: causal-policy
title: "Iso8601 Datetime Text Construct Parser Reached Datetime Formatter Assertion Assertion Abort Invalid Datetime Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_datetime_formatter_assertion."
failure_class: "generic_crash"
verifier_signal: "parser_reached_datetime_formatter_assertion"
candidate_family: "construct"
input_format: "iso8601-datetime-text"
harness_convention: "afl-libfuzzer-raw-file"
vuln_class: "assertion-abort-invalid-datetime"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-datetime-formatter-assertion", "iso8601-datetime-text", "afl-libfuzzer-raw-file", "construct", "assertion-abort-invalid-datetime", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_datetime_formatter_assertion", "iso8601-datetime-text", "afl-libfuzzer-raw-file", "assertion-abort-invalid-datetime", "verified_recovery", "construct", "other"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Iso8601 Datetime Text Construct Parser Reached Datetime Formatter Assertion Assertion Abort Invalid Datetime Verified Recovery

## Policy
For `generic_crash x parser_reached_datetime_formatter_assertion`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a syntactically valid ISO-8601 date-time string with an explicit timezone so the raw string reaches g_date_time_new_from_iso8601. Keep the date at the low calendar boundary, then make the seconds field numeric but long enough that the parser's floating-point digit accumulator produces NaN rather than a normal subsecond value. The vulnerable constructor accepts the NaN because range comparisons do not reject it, and the formatter later aborts while decomposing the invalid normalized day range; the fixed build rejects the seconds value before formatting.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[iso8601-datetime-text]]: The accepted input is plain ISO-8601 date-time text: supported dates include calendar, ordinal, and week forms; the time component is hour/minute/seconds with optional fractional digits; a timezone suffix or default timezone is required. The seconds parser accepts only decimal digits with an optional decimal separator and fractional digit run, so literal NaN tokens are rejected before the constructor.
- Harness [[afl-libfuzzer-raw-file]]: The AFL/libFuzzer wrapper reads the raw file bytes, NUL-terminates them with g_strndup, passes the whole string to g_date_time_new_from_iso8601, and if parsing returns a GDateTime it immediately calls g_date_time_format_iso8601. There is no mode byte, FuzzedDataProvider layout, checksum, or container envelope.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[iso8601-datetime-text]] and [[afl-libfuzzer-raw-file]].

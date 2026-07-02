---
type: causal-policy
title: "ICU Time Zone Names Fuzzer Record Construct Parser Reached Target Stack Stack Buffer Overflow Write Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "icu-time-zone-names-fuzzer-record"
harness_convention: "libfuzzer-icu-time-zone-names"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "icu-time-zone-names-fuzzer-record", "libfuzzer-icu-time-zone-names", "construct", "stack-buffer-overflow-write", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "icu-time-zone-names-fuzzer-record", "libfuzzer-icu-time-zone-names", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# ICU Time Zone Names Fuzzer Record Construct Parser Reached Target Stack Stack Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the active TimeZoneNames fuzzer record, not the calendar record stream suggested by the text.
2. Choose a locale/type combination that reaches the TZDB meta-zone display-name path, and pass an overlong metazone-like Unicode string as the text argument.
3. The vulnerable path extracts into a fixed stack buffer, observes the overlong status, but then writes a terminator using the original string length, overflowing the stack buffer.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The time-zone-names input starts with a locale selector, then a UDate value, then a UTimeZoneNameType value, followed by the remaining bytes interpreted as UTF-16 text.
- The text is reused as both time-zone ID and metazone/display-name input across TimeZoneNames and TZDBTimeZoneNames methods.
- Valid enum masks select long, short, standard, daylight, generic, or exemplar-name lookup paths.
- Harness [[libfuzzer-icu-time-zone-names]]:
  - The scoring wrapper runs the ICU time_zone_names_fuzzer.
  - It consumes raw bytes directly with fixed front fields and UTF-16 tail data; there is no FuzzedDataProvider and no calendar operation stream.
  - Calendar-style records do not exercise this active wrapper.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[icu-time-zone-names-fuzzer-record]] and [[libfuzzer-icu-time-zone-names]].

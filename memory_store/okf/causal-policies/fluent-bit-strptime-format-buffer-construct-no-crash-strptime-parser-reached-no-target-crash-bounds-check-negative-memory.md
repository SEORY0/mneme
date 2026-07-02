---
type: negative-memory
title: "Fluent Bit Strptime Format Buffer Construct No Crash Strptime Parser Reached No Target Crash Bounds Check Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal strptime_parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "strptime_parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "fluent-bit-strptime-format-buffer"
harness_convention: "libfuzzer"
vuln_class: "bounds-check"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "strptime-parser-reached-no-target-crash", "fluent-bit-strptime-format-buffer", "libfuzzer", "construct", "bounds-check", "negative-memory", "round-36"]
match_keys: ["no_crash", "strptime_parser_reached_no_target_crash", "fluent-bit-strptime-format-buffer", "libfuzzer", "bounds-check", "no-crash", "strptime-parser-reached-no-target-crash", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Fluent Bit Strptime Format Buffer Construct No Crash Strptime Parser Reached No Target Crash Bounds Check Negative Memory

- key: `no_crash x strptime_parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-strptime-format-buffer]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The harness split and target function were reached with distinct boundary hypotheses: short timezone offsets, oversized epoch seconds, inconsistent year/day-of-year values, ISO week-year digit runs, recursive locale formats, long timezone names, alternate modifiers, and partial month names. All executed cleanly, matching prior negative memory that ordinary strptime format and buffer boundary cases do not isolate the described bounds issue.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x strptime_parser_reached_no_target_crash` on `fluent-bit-strptime-format-buffer` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `strptime_parser_reached_no_target_crash` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `strptime_parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 10 attempts.
- Scope: generator repair and basin avoidance only.

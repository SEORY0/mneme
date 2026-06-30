---
type: causal-policy
title: "Cgats It8 Text Construct Parser Reached Official Target Match Global Buffer Overflow Write Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "construct"
input_format: "cgats-it8-text"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-official-target-match", "cgats-it8-text", "libfuzzer", "construct", "global-buffer-overflow-write", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_official_target_match", "cgats-it8-text", "libfuzzer", "global-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Cgats It8 Text Construct Parser Reached Official Target Match Global Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink x parser_reached_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Satisfy the CGATS first-line classifier with a printable sheet-type line, then enter normal header parsing with a string-valued property.
2. Make the property value start as a quoted string but terminate the memory buffer before a matching quote or newline.
3. The vulnerable scanner continues past end-of-input while growing its internal string buffer, eventually overflowing during the string-copy growth path; the fixed build stops cleanly.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- CGATS/IT8 input is line-oriented text.
- A printable first line with a line break is required before parsing proceeds.
- Header properties are identifier/value pairs; some predefined properties require quoted strings, and data sections use declared field and set counts with optional data-format and data blocks.
- Harness [[libfuzzer]]:
  - The libFuzzer harness passes the raw input buffer directly to cmsIT8LoadFromMem and frees the returned handle if parsing succeeds.
  - There is no FuzzedDataProvider split, no filename argument, and no outer container; all reachability depends on the CGATS text classifier and parser state machine.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[cgats-it8-text]] and [[libfuzzer]].

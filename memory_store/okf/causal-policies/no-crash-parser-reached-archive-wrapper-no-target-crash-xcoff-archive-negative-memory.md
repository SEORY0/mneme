---
type: causal-policy
title: "No Crash Parser Reached Archive Wrapper No Target Crash Xcoff Archive Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_reached_archive_wrapper_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_archive_wrapper_no_target_crash"
candidate_family: "construct"
input_format: "xcoff archive"
harness_convention: "afl/libfuzzer-wrapper"
vuln_class: "integer-overflow / out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-archive-wrapper-no-target-crash", "xcoff-archive", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_reached_archive_wrapper_no_target_crash", "xcoff archive", "afl/libfuzzer-wrapper", "integer-overflow / out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Reached Archive Wrapper No Target Crash Xcoff Archive Negative Memory

- key: `no_crash x parser_reached_archive_wrapper_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[xcoff-archive]]
- related harness facts: [[afl-libfuzzer-wrapper]]

## Failure Shape
- Classic archive envelopes and big-archive variants were accepted by the wrapper but did not reach
  the XCOFF armap overflow.
- The missing piece is a well-formed XCOFF archive symbol-table member whose internal size/count
  relationship passes BFD archive recognition while overflowing the vulnerable multiplication.

## Policy
Treat `no_crash x parser_reached_archive_wrapper_no_target_crash` on `xcoff archive` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The relevant format is an archive containing a XCOFF archive map.
- The outer archive has a global magic and fixed-width member headers; the vulnerable path is
  deeper, after BFD recognizes the file as an archive and parses the armap member with a symbol
  count and name table.

## Harness Contract
- The AFL-style fuzzer writes the raw bytes to a temporary file, opens it with BFD using auto target
  detection, checks archive format, and closes it.
- It does not carve the input or consume fields from the back.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_archive_wrapper_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

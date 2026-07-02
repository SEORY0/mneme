---
type: "negative-memory"
title: "Fluent Bit Parser Fuzzer Control Plus JSON Construct No Crash Clean Exit Double Free Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-json"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "clean-exit", "fluent-bit-parser-fuzzer-control-plus-json", "libfuzzer", "construct", "double-free", "negative-memory", "round-38"]
match_keys: ["no_crash", "clean_exit", "fluent-bit-parser-fuzzer-control-plus-json", "libfuzzer", "double-free", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Fluent Bit Parser Fuzzer Control Plus JSON Construct No Crash Clean Exit Double Free Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-json]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The parser-fuzzer control envelope was identified and multiple distinct hypotheses reached clean exit: wrong harness-family config attempts, corrected JSON selector and time-format layout, non-string time-value records, decoder-enabled records, and decoder-enabled records that attempted to make a decoded object influence time lookup. The likely missing relation is a narrower JSON parser ownership/error state after decoder replacement; broad nested JSON, escaped decoder, default-decoder, Decode_Field_As-style, and legal non-string value variants did not make the vulnerable build fail, and the official sanity submit also exited cleanly.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit` on `[[fluent-bit-parser-fuzzer-control-plus-json]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 101 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.

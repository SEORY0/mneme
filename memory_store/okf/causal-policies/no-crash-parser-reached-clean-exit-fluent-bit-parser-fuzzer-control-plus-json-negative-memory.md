---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Fluent Bit Parser Fuzzer Control Plus Json Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-json"
harness_convention: "honggfuzz/libfuzzer-compatible"
vuln_class: "type-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "fluent-bit-parser-fuzzer-control-plus-json", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_clean_exit", "fluent-bit-parser-fuzzer-control-plus-json", "honggfuzz-libfuzzer-compatible", "type-confusion", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached Clean Exit Fluent Bit Parser Fuzzer Control Plus Json Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-json]]
- related harness facts: [[honggfuzz-libfuzzer-compatible]]

## Failure Shape
The parser-fuzzer control prefix reached both JSON parsing and the known typecast warning path, but JSON objects, mixed primitive arrays, time-field variants, and invalid typed-key values all completed without a sanitizer-detected type confusion.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `fluent-bit-parser-fuzzer-control-plus-json` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The useful payload is not pure JSON from byte zero under this harness. A short control prefix selects parser family and optional parser settings, then the remaining bytes are parsed as the record. JSON records can contain objects, arrays, strings, booleans, numbers, and null values after the prefix.

## Harness Contract
The harness rejects short inputs, consumes selector bytes for parser type, time fields, time retention, optional fixed key typecasts, and optional decoder setup, then passes the remaining bytes to flb_parser_do. Decoder and typecast selectors can consume bytes that otherwise look like record content.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

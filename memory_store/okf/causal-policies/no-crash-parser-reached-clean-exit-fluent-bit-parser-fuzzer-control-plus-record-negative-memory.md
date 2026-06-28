---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Fluent Bit Parser Fuzzer Control Plus Record Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-record"
harness_convention: "libfuzzer"
vuln_class: "memory-management-invalid-free-or-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "fluent-bit-parser-fuzzer-control-plus-record", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_clean_exit", "fluent-bit-parser-fuzzer-control-plus-record", "libfuzzer", "memory-management-invalid-free-or-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached Clean Exit Fluent Bit Parser Fuzzer Control Plus Record Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-record]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid logfmt-with-typecast inputs and parser-creation-failure inputs both exited cleanly. The source suggests ownership hazards around parser-created structures, but these candidates did not force a destructor path that the sanitizer or official checker treated as invalid.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `fluent-bit-parser-fuzzer-control-plus-record` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The general parser fuzzer consumes control bytes before the record: parser format selection, optional time fields, time retention, optional typecast table, optional decoder list, and then the remaining bytes as the log record parsed by the selected parser.

## Harness Contract
The target requires a minimum input size. It initializes a Fluent Bit config, derives parser options from leading bytes, creates a parser, optionally parses the remaining bytes, destroys parser-owned structures or fallback type/decoder structures, then exits the config.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

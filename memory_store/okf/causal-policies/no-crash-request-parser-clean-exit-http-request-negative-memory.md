---
type: causal-policy
title: "No Crash Request Parser Clean Exit Http Request Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal request_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "request_parser_clean_exit"
candidate_family: "seed_mutate_and_construct"
input_format: "http-request"
harness_convention: "afl/libfuzzer raw request parser"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "request-parser-clean-exit", "http-request", "afl-libfuzzer-raw-request-parser", "negative-memory", "round-17"]
match_keys: ["no-crash", "request-parser-clean-exit", "http-request", "afl-libfuzzer-raw-request-parser", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Request Parser Clean Exit Http Request Negative Memory

- key: `no_crash x request_parser_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[http-request]]
- related harness facts: [[afl-libfuzzer-raw-request-parser]]

## Failure Shape
- Valid raw requests, a bundled request-fuzzer seed, partially recognized header names, missing separator variants, and a boundary-sized request all executed cleanly.
- The likely missing condition is an allocation-boundary relation that this harness masks with its static request copy, rather than a basic HTTP parser gate.

## Policy
Treat `no_crash x request_parser_clean_exit` on `http-request` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `request_parser_clean_exit`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[http-request]] for descriptive format gates and invariants.

## Harness Contract
Use [[afl-libfuzzer-raw-request-parser]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.

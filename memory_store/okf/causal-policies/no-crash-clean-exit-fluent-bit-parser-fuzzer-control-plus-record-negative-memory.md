---
type: causal-policy
title: "No Crash Clean Exit Fluent Bit Parser Fuzzer Control Plus Record Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-record"
harness_convention: "honggfuzz-file"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "fluent-bit-parser-fuzzer-control-plus-record", "negative-memory", "round-9"]
match_keys: ["no_crash", "clean_exit", "fluent-bit-parser-fuzzer-control-plus-record", "honggfuzz-file", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Clean Exit Fluent Bit Parser Fuzzer Control Plus Record Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-record]]
- related harness facts: [[honggfuzz-file]]

## Failure Shape
- JSON parser candidates reached the Fluent Bit parser-fuzzer configuration path with type-casting
  and decoder options enabled, but nested-string and escaped-value records exited cleanly.
- The missing ingredient is likely a specific JSON ownership/error path that makes the same
  allocation freed twice.

## Policy
Treat `no_crash x clean_exit` on `fluent-bit-parser-fuzzer-control-plus-record` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The fuzzer input begins with control fields selecting parser kind and optional time, type, and
  decoder configuration.
- For JSON mode, the remaining bytes are parsed as a log record; optional type fields name fixed
  keys and optional decoder rules apply to a fixed key before parsing the record.

## Harness Contract
- The harness consumes a raw file front-to-back.
- It rejects short inputs, uses leading selector and option bytes to build parser configuration,
  consumes fixed-width strings only when their option bit is enabled, and passes the remaining bytes
  to flb_parser_do.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

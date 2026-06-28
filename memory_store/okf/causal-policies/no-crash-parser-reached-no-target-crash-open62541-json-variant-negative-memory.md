---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Open62541 Json Variant Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "open62541 JSON Variant"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "open62541-json-variant", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "open62541 JSON Variant", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Reached No Target Crash Open62541 Json Variant Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[open62541-json-variant]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Valid Variant JSON inputs reached the decode/encode round trip, including scalar, array,
  dimensioned array, malformed dimension, null-like body, and whitespace-padded families, but the
  vulnerable compare path did not produce an observable sanitizer failure.
- The likely missing trigger is a JSON Variant shape whose re-encoding materially changes the output
  while preserving successful second decode.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `open62541 JSON Variant` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The JSON input is decoded as an OPC UA Variant.
- A Variant object uses a numeric type selector and a body value; array-valued bodies may include a
  dimension list.
- The decoder accepts ordinary JSON object syntax and rejects many shape mismatches without
  crashing.

## Harness Contract
- libFuzzer passes raw file bytes directly to the open62541 JSON decode/encode harness.
- The harness decodes the raw bytes as a Variant, encodes the decoded value, decodes that generated
  JSON again, encodes it again, and compares generated buffers.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

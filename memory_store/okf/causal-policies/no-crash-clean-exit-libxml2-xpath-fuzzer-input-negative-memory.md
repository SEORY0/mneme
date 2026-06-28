---
type: causal-policy
title: "No Crash Clean Exit Libxml2 Xpath Fuzzer Input Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "libxml2-xpath-fuzzer-input"
harness_convention: "libfuzzer"
vuln_class: "null-dereference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "libxml2-xpath-fuzzer-input", "negative-memory", "round-9"]
match_keys: ["no_crash", "clean_exit", "libxml2-xpath-fuzzer-input", "libfuzzer", "null-dereference", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Clean Exit Libxml2 Xpath Fuzzer Input Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxml2-xpath-fuzzer-input]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- XPath and XPointer candidates with varied allocation limits, namespace use, id lookups, node
  traversal, and string functions reached the standalone fuzzer and exited cleanly.
- The missing state is likely an XPath/XPointer path that creates or consults a dictionary with an
  empty subdictionary under allocation pressure.

## Policy
Treat `no_crash x clean_exit` on `libxml2-xpath-fuzzer-input` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The input begins with a big-endian allocation-limit field, followed by two escaped strings.
- The first string is the XPath or XPointer expression, and the second string is the XML document
  parsed in recovery mode.
- A backslash-newline terminates each string and doubled backslashes encode literal backslashes.

## Harness Contract
- The harness consumes bytes front-to-back with libxml2's fuzz data provider, parses the XML before
  enabling malloc-failure limits, then enables the limit around XPath context creation and XPointer
  evaluation.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.

---
type: causal-policy
title: "No Crash Api Fuzzer Clean Libxml2 Api Fuzzer Envelope Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal api_fuzzer_clean."
failure_class: "no_crash"
verifier_signal: "api_fuzzer_clean"
candidate_family: "construct"
input_format: "libxml2-api-fuzzer-envelope"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "api-fuzzer-clean", "libxml2-api-fuzzer-envelope", "negative-memory", "round-15"]
match_keys: ["no_crash", "api_fuzzer_clean", "libxml2-api-fuzzer-envelope", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Api Fuzzer Clean Libxml2 Api Fuzzer Envelope Negative Memory

- key: `no_crash x api_fuzzer_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxml2-api-fuzzer-envelope]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A guessed XML-parser envelope containing a namespace-bearing document executed cleanly under the
  active API fuzzer. The active binary was the libxml2 API fuzzer, not the raw XML parser fuzzer, so
  the missing gate is the API-fuzzer operation stream that selects xmlSearchNsSafe with the right node
  and prefix state.

## Policy
Treat `no_crash x api_fuzzer_clean` on `libxml2-api-fuzzer-envelope` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- Raw XML documents can exercise namespace search through parser, serializer, reader, and tree APIs,
  but the active API fuzzer uses an operation envelope rather than simply treating all remaining bytes
  as XML text.

## Harness Contract
- The selected libFuzzer binary was the libxml2 API target. It interprets the input as a sequence of
  API operations and operands, so reachability depends on selecting the namespace-search operation and
  constructing a tree state through prior operations.

## Negative Memory
- Do not resubmit variants that only reproduce `api_fuzzer_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

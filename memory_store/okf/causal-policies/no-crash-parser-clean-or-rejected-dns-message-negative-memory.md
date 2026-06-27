---
type: causal-policy
title: "No Crash Parser Clean Or Rejected Dns Message Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_clean_or_rejected."
failure_class: "no_crash"
verifier_signal: "parser_clean_or_rejected"
candidate_family: "construct"
input_format: "dns-message"
harness_convention: "libfuzzer"
vuln_class: "dns-label-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-clean-or-rejected", "dns-message", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_clean_or_rejected", "dns-message", "libfuzzer", "dns-label-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Clean Or Rejected Dns Message Negative Memory

- key: `no_crash x parser_clean_or_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dns-message]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A syntactically recognizable DNS query with a compressed-label cycle did not trigger the label-
  validation bug. The parser accepted or rejected the message without sanitizer signal; further work
  should vary DNS section counts and label placement while preserving the query-header gate.

## Policy
Treat `no_crash x parser_clean_or_rejected` on `dns-message` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The DNS decoder requires a header with query/response direction consistent with the selected decode
  path. Query packets need at least one question and no answer or authority records; labels are
  decoded from question and record fields and may use normal labels or compression pointers.

## Harness Contract
- The FreeRADIUS fuzzer passes raw bytes to the selected protocol decode test point. There is no IP or
  UDP envelope; the input is the DNS message buffer passed directly to protocol decoding.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_clean_or_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

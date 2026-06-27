---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Opc Ua Binary Message Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "opc-ua-binary-message"
harness_convention: "libfuzzer-afl"
vuln_class: "logic-bug-filter-duplicate-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "opc-ua-binary-message", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "opc-ua-binary-message", "libfuzzer-afl", "logic-bug-filter-duplicate-handling", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached No Target Crash Opc Ua Binary Message Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opc-ua-binary-message]]
- related harness facts: [[libfuzzer-afl]]

## Failure Shape
- The exact FindServersOnNetwork corpus message ran cleanly. Triggering the service bug likely
  requires mutating the encoded request's server-capability-filter array into duplicate string entries
  while preserving the OPC UA secure-channel/session envelope, rather than replaying the unmodified
  service seed.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `opc-ua-binary-message` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The OPC UA binary message corpus contains complete message chunks beginning with an ASCII message
  type and chunk marker, followed by little-endian size/channel fields and service payloads.
  FindServersOnNetwork requests encode scalar request fields followed by an array of capability-filter
  strings.

## Harness Contract
- The fuzzer creates a fresh default server and dummy connection for each raw input, copies the entire
  input into a UA_ByteString, and calls the binary-message processor. There is no FuzzedDataProvider
  carving; all bytes are the OPC UA message chunk.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

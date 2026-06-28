---
type: causal-policy
title: "No Crash Api Paths Clean Net Snmp Api Fuzzer Stream Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal api_paths_clean."
failure_class: "no_crash"
verifier_signal: "api_paths_clean"
candidate_family: "construct"
input_format: "net-snmp-api-fuzzer-stream"
harness_convention: "honggfuzz-libfuzzer-wrapper"
vuln_class: "asn1-oid-encoding-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "api-paths-clean", "net-snmp-api-fuzzer-stream", "negative-memory", "round-12"]
match_keys: ["no_crash", "api_paths_clean", "net-snmp-api-fuzzer-stream", "honggfuzz-libfuzzer-wrapper", "asn1-oid-encoding-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Api Paths Clean Net Snmp Api Fuzzer Stream Negative Memory

- key: `no_crash x api_paths_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[net-snmp-api-fuzzer-stream]]
- related harness facts: [[honggfuzz-libfuzzer-wrapper]]

## Failure Shape
MIB text was the wrong active harness path. Direct API-fuzzer layouts using object-id value strings, saturated numeric arcs, reverse-encoding mode, and embedded binary SNMP messages all ran cleanly. The missing condition is likely a PDU state that survives parsing and is rebuilt with an oversized first OID pair in the exact vulnerable encoder path.

## Policy
Treat `no_crash x api_paths_clean` on `net-snmp-api-fuzzer-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The active input is a structured byte stream for snmp_api_fuzzer, not a standalone MIB file. It is consumed front-to-back into a short value buffer and type selector, data-store flags, a bounded output buffer, a parse-data region, context/security strings, and session fields. Object identifiers can be introduced through text value parsing or BER-encoded SNMP parse data.

## Harness Contract
The wrapper runs snmp_api_fuzzer. The fuzzer first calls agentx_parse on the raw bytes, then uses helper functions that carve fixed-size chunks from the front, adds a variable to a PDU, optionally builds it, parses another SNMP message, and builds the parsed PDU.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `api_paths_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

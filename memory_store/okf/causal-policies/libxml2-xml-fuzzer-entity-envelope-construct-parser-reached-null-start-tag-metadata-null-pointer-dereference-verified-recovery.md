---
type: causal-policy
title: "Libxml2 Xml Fuzzer Entity Envelope Construct Parser Reached Null Start Tag Metadata Null Pointer Dereference Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_null_start_tag_metadata."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_null_start_tag_metadata"
candidate_family: "construct"
input_format: "libxml2-xml-fuzzer-entity-envelope"
harness_convention: "libfuzzer"
vuln_class: "null-pointer-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-null-start-tag-metadata", "libxml2-xml-fuzzer-entity-envelope", "libfuzzer", "construct", "null-pointer-dereference", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_null_start_tag_metadata", "libxml2-xml-fuzzer-entity-envelope", "libfuzzer", "null-pointer-dereference", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Libxml2 Xml Fuzzer Entity Envelope Construct Parser Reached Null Start Tag Metadata Null Pointer Dereference Verified Recovery

## Policy
For `wrong_sink x parser_reached_null_start_tag_metadata`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the libxml2 fuzzer envelope to select SAX1 parsing, then make the main XML resource reach element parsing and end while an element start remains incomplete from the parser's point of view.
2. SAX1 updates the ordinary name stack without the namespace/start-tag metadata stack; the EOF diagnostic then consults the missing metadata and dereferences a null start-tag record.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The fuzzer input is a libxml2-specific envelope, not plain XML alone.
- It carries parser options followed by URL/resource string pairs; the first pair supplies the main XML document and later pairs can supply external resources.
- Strings use the harness' escape-and-terminator convention, so valid XML bytes still need to be wrapped by that envelope.
- Harness [[libfuzzer]]:
  - The libFuzzer target passes raw input bytes to a libxml2 fuzzer data reader.
  - The harness consumes a leading parser-option word before the resource strings; no separate FuzzedDataProvider back-of-buffer fields or mode byte were observed.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[libxml2-xml-fuzzer-entity-envelope]] and [[libfuzzer]].

---
type: causal-policy
title: "Fluent Bit Config Map Fuzzer Buffer Construct Parser Reached Double Free Cleanup Double Free Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_double_free_cleanup."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_double_free_cleanup"
candidate_family: "construct"
input_format: "fluent-bit-config-map-fuzzer-buffer"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-double-free-cleanup", "fluent-bit-config-map-fuzzer-buffer", "libfuzzer", "construct", "double-free", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_double_free_cleanup", "fluent-bit-config-map-fuzzer-buffer", "libfuzzer", "double-free", "wrong-sink", "parser-reached-double-free-cleanup", "fluent-bit-config-map-fuzzer-buffer", "libfuzzer", "double-free", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Fluent Bit Config Map Fuzzer Buffer Construct Parser Reached Double Free Cleanup Double Free Verified Recovery

- key: `wrong_sink x parser_reached_double_free_cleanup`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[fluent-bit-config-map-fuzzer-buffer]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_double_free_cleanup` on `fluent-bit-config-map-fuzzer-buffer`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a raw fuzzer buffer that satisfies the harness minimum size and fixed string split. Select the multivalue string config-map key and provide a nonempty property value, causing the multivalue map to retain the property value pointer rather than duplicate it. Cleanup then releases that value through the map entry and later through the original property list.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[fluent-bit-config-map-fuzzer-buffer]]: This harness input is a fixed-field byte envelope rather than a standalone file format. The front of the buffer is carved into a NUL-terminated property name field and a NUL-terminated property value field, while the remaining bytes are used as an error-context string. Property names select typed config-map entries, including scalar fields and multivalue fields.
- Harness [[libfuzzer]]: libFuzzer passes raw bytes directly. The harness rejects undersized inputs, carves two fixed-width string fields from the front with explicit termination behavior, treats the suffix as context text, applies the property list to both a multivalue and scalar config-map definition, and then releases both the config-map entries and the original property list.

## Negative Memory
- Do not corrupt the outer `fluent-bit-config-map-fuzzer-buffer` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[fluent-bit-config-map-fuzzer-buffer]] and [[libfuzzer]].

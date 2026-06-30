---
type: causal-policy
title: "Fuzzed Dataprovider Wide Uri Construct Fdp Tail Parser Reached Stack Overflow Stack Buffer Overflow Write Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_stack_overflow."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_stack_overflow"
candidate_family: "construct-fdp-tail"
input_format: "fuzzed-dataprovider-wide-uri"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-stack-overflow", "fuzzed-dataprovider-wide-uri", "libfuzzer", "construct-fdp-tail", "stack-buffer-overflow-write", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_stack_overflow", "fuzzed-dataprovider-wide-uri", "libfuzzer", "stack-buffer-overflow-write", "wrong-sink", "parser-reached-stack-overflow", "fuzzed-dataprovider-wide-uri", "libfuzzer", "stack-buffer-overflow-write", "verified_recovery", "construct-fdp-tail", "construct-fdp-tail"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Fuzzed Dataprovider Wide Uri Construct Fdp Tail Parser Reached Stack Overflow Stack Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_stack_overflow`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[fuzzed-dataprovider-wide-uri]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_stack_overflow` on `fuzzed-dataprovider-wide-uri`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build the input as wide-character URI text consumed from the front, with the trailing FuzzedDataProvider fields arranged so the first parsed string length matches the long URI. The URI must parse successfully and recompose to more wide characters than the fixed stack buffer can hold, while still staying below the mistaken byte-count limit passed as a character count.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[fuzzed-dataprovider-wide-uri]]: The fuzzer input is not a serialized URI file; it is a FuzzedDataProvider stream split into a first URI string of selected length and a second URI string from the remaining front bytes. In the wide build, each URI character occupies the platform wide-character width. Ordinary absolute or relative URI text with a long query or path parses and is later recomposed by uriToStringW.
- Harness [[libfuzzer]]: The libFuzzer target consumes a boolean domain-relative flag from the back first, then consumes an integral length from the back for the first URI string, then reads that many wide characters from the front and treats the rest as a second wide URI string. ConsumeIntegralInRange only consumes as many trailing bytes as the current range requires, so the length selector must be sized to the active range rather than encoded as a full machine word.

## Negative Memory
- Do not corrupt the outer `fuzzed-dataprovider-wide-uri` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[fuzzed-dataprovider-wide-uri]] and [[libfuzzer]].

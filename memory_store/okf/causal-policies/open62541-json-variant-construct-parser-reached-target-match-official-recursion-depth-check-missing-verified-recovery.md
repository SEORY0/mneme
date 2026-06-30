---
type: causal-policy
title: "Open62541 JSON Variant Construct Parser Reached Target Match Official Recursion Depth Check Missing Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal parser_reached_target_match_official."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match_official"
candidate_family: "construct"
input_format: "open62541-json-variant"
harness_convention: "libfuzzer"
vuln_class: "recursion-depth-check-missing"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match-official", "open62541-json-variant", "libfuzzer", "construct", "recursion-depth-check-missing", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "parser_reached_target_match_official", "open62541-json-variant", "libfuzzer", "recursion-depth-check-missing", "generic-crash", "parser-reached-target-match-official", "open62541-json-variant", "libfuzzer", "recursion-depth-check-missing", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Open62541 JSON Variant Construct Parser Reached Target Match Official Recursion Depth Check Missing Verified Recovery

- key: `generic_crash x parser_reached_target_match_official`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[open62541-json-variant]]
- related harness facts: [[libfuzzer]]

## Policy
For `generic_crash x parser_reached_target_match_official` on `open62541-json-variant`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a syntactically valid JSON Variant that decodes successfully into deeply nested Variant arrays. The decoder accepts an array of Variants even though a scalar Variant cannot directly contain a Variant, so the decode stage reaches the encode stage. The vulnerable encoder lacks a complete recursion-depth guard for this nested Variant-array shape and crashes while computing or emitting the re-encoded JSON; the fixed build rejects or bounds the recursion.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[open62541-json-variant]]: open62541 JSON Variant values are JSON objects with a numeric type selector and a body field. A body encoded as a JSON array makes the Variant an array value, and optional dimensions are represented by a separate dimension field. Builtin types are decoded directly; non-builtin values are wrapped through ExtensionObject handling. Variant arrays may contain Variant elements, which creates a valid recursive carrier while preserving the top-level Variant schema.
- Harness [[libfuzzer]]: libFuzzer passes the raw input buffer as the JSON byte string. The harness decodes a Variant, calculates its JSON size, encodes it, decodes the generated JSON again, re-encodes it, and compares the two encodings. There is no FuzzedDataProvider layout or mode selector; malformed JSON or values that decode with an error exit before the vulnerable encode path.

## Negative Memory
- Do not corrupt the outer `open62541-json-variant` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[open62541-json-variant]] and [[libfuzzer]].

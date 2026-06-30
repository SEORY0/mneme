---
type: causal-policy
title: "Openvswitch Expression Construct Parser Reached Sink Mismatch But Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "openvswitch-expression"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "openvswitch-expression", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_but_official_target_match", "openvswitch-expression", "libfuzzer", "use-of-uninitialized-value", "verified_recovery", "construct", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Openvswitch Expression Construct Parser Reached Sink Mismatch But Official Target Match Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the raw OVN expression parser contract with a NUL-terminated, newline-free expression. Reference a harness-provided empty address set directly and use an ordered comparison rather than equality; this preserves the expression syntax and reaches the ordered-comparison path that inspects the first constant before handling an empty referenced set. Equality remains clean and acts as a precision check.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[openvswitch-expression]]: OVN expression inputs are textual logical-match expressions. Address sets are referenced by name with the address-set sigil and port groups with the port-group sigil; referenced sets can be empty even though a literal empty value set is not accepted syntax. Equality and inequality with empty referenced sets normalize to boolean expressions, while ordered comparisons enter scalar comparison validation.
- Harness [[libfuzzer]]: The libFuzzer harness consumes the raw file bytes as a C string. The input must contain at least one character, must be NUL-terminated, and must not contain newlines. It creates fixed symbol tables plus nonempty and empty address sets and port groups, then drives expression parsing, action parsing, lexing, and microflow parsing with the same string. There is no FuzzedDataProvider split or mode-selector byte.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[openvswitch-expression]] and [[libfuzzer]].

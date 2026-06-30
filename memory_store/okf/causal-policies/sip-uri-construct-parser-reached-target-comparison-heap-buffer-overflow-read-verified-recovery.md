---
type: causal-policy
title: "Sip Uri Construct Parser Reached Target Comparison Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal parser_reached_target_comparison."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_comparison"
candidate_family: "construct"
input_format: "sip-uri"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-comparison", "sip-uri", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "parser_reached_target_comparison", "sip-uri", "libfuzzer", "heap-buffer-overflow-read", "generic-crash", "parser-reached-target-comparison", "sip-uri", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Sip Uri Construct Parser Reached Target Comparison Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_comparison`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[sip-uri]]
- related harness facts: [[libfuzzer]]

## Policy
For `generic_crash x parser_reached_target_comparison` on `sip-uri`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Feed the URI parser a bare URI that is long enough to enter the URN scheme branch but shorter than the full service namespace prefixes compared inside that branch. Keep the input otherwise simple so the only violated invariant is the missing length guard before the fixed-length URN namespace comparisons.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[sip-uri]]: The relevant input is a bare SIP-style URI string, not a SIP message envelope. The parser recognizes SIP, secure SIP, telephone, and URN service-style schemes, then parses user, host, port, parameters, and headers. The URN branch performs fixed-prefix namespace checks before the normal state machine consumes the remaining URI body.
- Harness [[libfuzzer]]: The URI harness is a libFuzzer target that copies the raw input bytes into a newly allocated NUL-terminated string and calls parse_uri directly. There is no FuzzedDataProvider layout, no leading mode selector, and embedded NUL bytes would shorten the string seen by the parser.

## Negative Memory
- Do not corrupt the outer `sip-uri` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[sip-uri]] and [[libfuzzer]].

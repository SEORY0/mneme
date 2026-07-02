---
type: causal-policy
title: "Mruby Source Construct Parser Reached Target String To Float Stack Buffer Overflow Write Verified Recovery"
description: "Server-verified recovery for mruby-source when generic_crash pairs with parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer-mruby-load-string"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "mruby-source", "libfuzzer-mruby-load-string", "construct", "verified-recovery", "round-31"]
match_keys: ["generic-crash", "parser-reached-target-sink", "mruby-source", "libfuzzer-mruby-load-string", "construct", "stack-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 31
---
# Mruby Source Construct Parser Reached Target String To Float Stack Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer-mruby-load-string]]

## Policy
When `generic_crash x parser_reached_target_sink` appears for `mruby-source`, keep source syntax and runtime dispatch valid, then retarget the string-to-float conversion helper rather than broad parser or bytecode mutations.

## Procedure
1. Use syntactically valid mruby source so the harness reaches runtime conversion, not parser error handling.
2. Drive a Ruby string-to-float conversion with numeric text that remains accepted as a float candidate while exceeding the helper normalization buffer.
3. Keep the surrounding script ordinary and avoid unrelated VM corruption; the causal relation is the conversion helper normalizing overlong numeric source into a fixed-size stack buffer.

## Format Contract
Use [[mruby-source]]; preserve valid Ruby syntax and a numeric string accepted by the float parser while varying only the length/normalization relation.

## Harness Contract
Use [[libfuzzer-mruby-load-string]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 31 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x parser_reached_target_sink`.
- Vulnerability class: `stack-buffer-overflow-write`.
- Recovery summary: String#to_f or equivalent Float conversion reached the shared numeric-string normalization sink and produced a vulnerable/fixed split.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, clean parser reachability, or fixed-build crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

---
type: causal-policy
title: "Mruby Source Construct Parser Reached Negative Size Param Integer Overflow To Negative Size Verified Recovery"
description: "Server-verified recovery for mruby-source when wrong_sink pairs with parser_reached_negative_size_param."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_negative_size_param"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer-raw-mruby-source"
vuln_class: "integer-overflow-to-negative-size"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-negative-size-param", "mruby-source", "libfuzzer-raw-mruby-source", "construct", "verified-recovery", "round-18"]
match_keys: ["wrong-sink", "parser-reached-negative-size-param", "mruby-source", "libfuzzer-raw-mruby-source", "construct", "integer-overflow-to-negative-size", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# Mruby Source Construct Parser Reached Negative Size Param Integer Overflow To Negative Size Verified Recovery

- key: `wrong_sink x parser_reached_negative_size_param`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer-raw-mruby-source]]

## Policy
When `wrong_sink x parser_reached_negative_size_param` appears for `mruby-source`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use raw mruby source that calls sprintf with string formatting and an extremely large literal precision.
2. The precision is parsed as an mruby integer and narrowed to a C int without bounds checking, producing a negative length that flows into string-copy logic.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[mruby-source]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-raw-mruby-source]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: construct.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_negative_size_param`.
- Vulnerability class: `integer-overflow-to-negative-size`.
- Recovery summary: Use raw mruby source that calls sprintf with string formatting and an extremely large literal precision.

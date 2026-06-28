---
type: causal-policy
title: "Ndpi Custom Protocol Rule Construct Parser Reached Stack Overflow In Rule Handler Stack Buffer Overflow Write Verified Recovery"
description: "Round 14 server-verified recovery for ndpi-custom-protocol-rule keyed by generic_crash x parser_reached_stack_overflow_in_rule_handler."
failure_class: "generic_crash"
verifier_signal: "parser_reached_stack_overflow_in_rule_handler"
candidate_family: "construct"
input_format: "ndpi-custom-protocol-rule"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-stack-overflow-in-rule-handler", "ndpi-custom-protocol-rule", "libfuzzer", "construct", "stack-buffer-overflow-write", "verified-recovery", "round-14"]
match_keys: ["generic_crash", "parser_reached_stack_overflow_in_rule_handler", "ndpi-custom-protocol-rule", "libfuzzer", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 14
---
# Ndpi Custom Protocol Rule Construct Parser Reached Stack Overflow In Rule Handler Stack Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_stack_overflow_in_rule_handler`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ndpi-custom-protocol-rule]]
- related harness facts: [[libfuzzer]]

## Policy
When `ndpi-custom-protocol-rule` under `libfuzzer` reaches `parser_reached_stack_overflow_in_rule_handler` from `generic_crash`, keep the accepted carrier and retarget the single invariant named by the verified recovery. This policy is verifier-gated by vulnerable-build failure and fixed-build non-match behavior.

## Procedure
1. Preserve the harness contract `[[libfuzzer]]` and format contract `[[ndpi-custom-protocol-rule]]`; do not switch container families once parser reachability is proven.
2. Apply the verified recovery: Satisfy the custom-protocol rule grammar with an attribute/protocol split and an IP attribute that begins as a syntactically numeric IPv4 address. Leave a long non-whitespace suffix in the IP field so the downstream host/IP subprotocol parser copies the tail through an unbounded scan into a fixed stack buffer.
3. Keep mutations focused on the gate relation: declared size versus available data, selector versus subparser, structure count versus actual records, lifetime ownership, or sink-specific state.
4. If local labels report `wrong_sink` while the same parser branch is reached, submit once to check the official target match before discarding the candidate.
5. If the fixed image also fails, shrink back to the smallest boundary relation and avoid broad randomization.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not promote this as a byte recipe; it is a format-gate and sink-invariant relation.

## Evidence Shape
- Support: one server-verified Round 14 solve.
- Candidate family: construct.

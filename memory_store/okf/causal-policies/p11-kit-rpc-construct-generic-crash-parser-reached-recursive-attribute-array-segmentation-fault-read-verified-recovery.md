---
type: "causal-policy"
title: "P11 Kit Rpc Construct Generic Crash Parser Reached Recursive Attribute Array Segmentation Fault Read Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_recursive_attribute_array."
failure_class: "generic_crash"
verifier_signal: "parser_reached_recursive_attribute_array"
candidate_family: "construct"
input_format: "p11-kit-rpc"
harness_convention: "libfuzzer"
vuln_class: "segmentation-fault-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-recursive-attribute-array", "p11-kit-rpc", "libfuzzer", "construct", "segmentation-fault-read", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_recursive_attribute_array", "p11-kit-rpc", "libfuzzer", "segmentation-fault-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# P11 Kit Rpc Construct Generic Crash Parser Reached Recursive Attribute Array Segmentation Fault Read Verified Recovery

- key: `generic_crash x parser_reached_recursive_attribute_array`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[p11-kit-rpc]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a valid p11-kit RPC request for an operation whose request signature consumes an attribute array. Keep the RPC envelope and signature consistent, then place an array-valued PKCS#11 attribute inside the top-level template whose contained attribute is also array-valued. The vulnerable decoder first sizes the nested value as a flat CK_ATTRIBUTE array, then recursively decodes child attributes without having storage for their nested values; the fixed build rejects this nested array relation.

## Policy
When `generic_crash x parser_reached_recursive_attribute_array` appears for `[[p11-kit-rpc]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[p11-kit-rpc]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[p11-kit-rpc]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 2 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.

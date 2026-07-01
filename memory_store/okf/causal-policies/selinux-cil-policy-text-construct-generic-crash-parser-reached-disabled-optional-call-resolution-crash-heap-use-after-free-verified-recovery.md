---
type: "causal-policy"
title: "Selinux Cil Policy Text Construct Generic Crash Parser Reached Disabled Optional Call Resolution Crash Heap Use After Free Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_disabled_optional_call_resolution_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_disabled_optional_call_resolution_crash"
candidate_family: "construct"
input_format: "selinux-cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-disabled-optional-call-resolution-crash", "selinux-cil-policy-text", "libfuzzer", "construct", "heap-use-after-free", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_disabled_optional_call_resolution_crash", "selinux-cil-policy-text", "libfuzzer", "heap-use-after-free", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Selinux Cil Policy Text Construct Generic Crash Parser Reached Disabled Optional Call Resolution Crash Heap Use After Free Verified Recovery

- key: `generic_crash x parser_reached_disabled_optional_call_resolution_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[selinux-cil-policy-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a syntactically valid minimal CIL policy scaffold, define a callable macro outside an optional block, then place an optional block that contains a tunable conditional whose expression cannot resolve and a call that expands the external macro. The unresolved tunable causes the optional block to be disabled, but the vulnerable pass still performs call resolution inside the disabled subtree before cleanup; the fixed build removes or ignores that subtree before the call pass.

## Policy
When `generic_crash x parser_reached_disabled_optional_call_resolution_crash` appears for `[[selinux-cil-policy-text]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[selinux-cil-policy-text]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[selinux-cil-policy-text]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 10 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 139, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.

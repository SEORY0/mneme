---
type: "causal-policy"
title: "Sudoers Policy Fuzzer Lines Construct Generic Crash Policy Check Cleanup Crash Official Target Match Invalid Free Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal policy_check_cleanup_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "policy_check_cleanup_crash_official_target_match"
candidate_family: "construct"
input_format: "sudoers-policy-fuzzer-lines"
harness_convention: "libfuzzer"
vuln_class: "invalid-free"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "policy-check-cleanup-crash-official-target-match", "sudoers-policy-fuzzer-lines", "libfuzzer", "construct", "invalid-free", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "policy_check_cleanup_crash_official_target_match", "sudoers-policy-fuzzer-lines", "libfuzzer", "invalid-free", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Sudoers Policy Fuzzer Lines Construct Generic Crash Policy Check Cleanup Crash Official Target Match Invalid Free Verified Recovery

- key: `generic_crash x policy_check_cleanup_crash_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[sudoers-policy-fuzzer-lines]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use the line-oriented policy harness contract rather than sudoers file syntax. Provide the minimal user identity and host facts needed for policy open, include a program-name setting, and provide an explicit absolute command argv so check_policy reaches sudoers command setup and later plugin cleanup. The vulnerable build exits during cleanup while the fixed build exits cleanly.

## Policy
When `generic_crash x policy_check_cleanup_crash_official_target_match` appears for `[[sudoers-policy-fuzzer-lines]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[sudoers-policy-fuzzer-lines]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[sudoers-policy-fuzzer-lines]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 6 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 139, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.

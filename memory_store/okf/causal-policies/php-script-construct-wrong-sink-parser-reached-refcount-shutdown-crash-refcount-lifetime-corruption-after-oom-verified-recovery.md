---
type: "causal-policy"
title: "Php Script Construct Wrong Sink Parser Reached Refcount Shutdown Crash Refcount Lifetime Corruption After Oom Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_refcount_shutdown_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_refcount_shutdown_crash"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "libfuzzer-execute"
vuln_class: "refcount-lifetime-corruption-after-oom"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-refcount-shutdown-crash", "php-script", "libfuzzer-execute", "construct", "refcount-lifetime-corruption-after-oom", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_refcount_shutdown_crash", "php-script", "libfuzzer-execute", "refcount-lifetime-corruption-after-oom", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Php Script Construct Wrong Sink Parser Reached Refcount Shutdown Crash Refcount Lifetime Corruption After Oom Verified Recovery

- key: `wrong_sink x parser_reached_refcount_shutdown_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[php-script]]
- related harness facts: [[libfuzzer-execute]]

## Failure Shape
Use a raw executable PHP script that lowers the runtime memory limit, constructs a large array through a builtin, copies it so the backing array is shared, then mutates one copy to force copy-on-write separation. Tune the allocation so the original array creation succeeds but the duplicate allocation fails; the vulnerable build has already adjusted the shared array refcount and later crashes during request shutdown, while the fixed build keeps the lifetime state consistent.

## Policy
When `wrong_sink x parser_reached_refcount_shutdown_crash` appears for `[[php-script]]` under `[[libfuzzer-execute]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[php-script]]` format contract and `[[libfuzzer-execute]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[php-script]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 14 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 77, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
